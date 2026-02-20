from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO
import time

from graph_builder import build_graph
from detectors.cycles import detect_cycles
from detectors.smurfing import detect_smurfing
from detectors.shell_networks import detect_shell_networks
from scoring import compute_scores
from schema import build_response

router = APIRouter()

MAX_ROWS = 20000  # safety limit


@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    start_time = time.perf_counter()

    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    contents = await file.read()
    if not contents:
        raise HTTPException(status_code=400, detail="Uploaded CSV file is empty.")

    try:
        df = pd.read_csv(BytesIO(contents), encoding="utf-8-sig")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read CSV: {e}")

    df.columns = [c.strip() for c in df.columns]

    if df.empty:
        raise HTTPException(status_code=400, detail="CSV contains no rows.")

    if len(df) > MAX_ROWS:
        raise HTTPException(
            status_code=413,
            detail=f"CSV too large. Max {MAX_ROWS} rows allowed."
        )

    required_cols = {
        "transaction_id",
        "sender_id",
        "receiver_id",
        "amount",
        "timestamp"
    }

    missing = required_cols - set(df.columns)

    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Missing columns: {', '.join(missing)}"
        )

    transactions = df.to_dict(orient="records")

    # Build graph
    graph = build_graph(transactions)

    # Performance filtering
    active_nodes = [n for n in graph.nodes() if graph.degree(n) >= 2]
    subgraph = graph.subgraph(active_nodes).copy()

    MAX_ANALYSIS_NODES = 5000

    if subgraph.number_of_nodes() > MAX_ANALYSIS_NODES:
        high_degree_nodes = sorted(
            subgraph.nodes(),
            key=lambda n: subgraph.degree(n),
            reverse=True
        )[:MAX_ANALYSIS_NODES]

        subgraph = subgraph.subgraph(high_degree_nodes).copy()

    # Run detectors
    rings = []
    rings.extend(detect_cycles(subgraph))
    rings.extend(detect_smurfing(transactions))
    rings.extend(detect_shell_networks(subgraph))

    # Compute scores
    suspicious_accounts, fraud_rings = compute_scores(rings)

    elapsed = time.perf_counter() - start_time

    return build_response(
        suspicious_accounts=suspicious_accounts,
        fraud_rings=fraud_rings,
        total_accounts=len(graph.nodes),
        processing_time=round(elapsed, 3)
    )
