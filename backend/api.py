from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

from graph_builder import build_graph
from detectors.cycles import detect_cycles
from detectors.smurfing import detect_smurfing
from detectors.shell_networks import detect_shell_networks
from scoring import compute_scores
from schema import build_response

router = APIRouter()

MAX_ROWS = 20000  # safety limit for large CSVs

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    # 1. Basic filename validation
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    # 2. Read file contents once
    contents = await file.read()
    if not contents or len(contents) == 0:
        raise HTTPException(status_code=400, detail="Uploaded CSV file is empty.")

    # 3. Parse CSV robustly (handle BOM, encoding issues)
    try:
        df = pd.read_csv(BytesIO(contents), encoding="utf-8-sig")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read CSV: {e}")

    # 4. Clean column names (strip spaces)
    df.columns = [c.strip() for c in df.columns]

    if df.empty:
        raise HTTPException(status_code=400, detail="CSV parsed successfully but contains no rows.")

    # 5. Guardrail for very large files
    if len(df) > MAX_ROWS:
        raise HTTPException(
            status_code=413,
            detail=f"CSV too large. Max {MAX_ROWS} rows allowed."
        )

    # 6. Validate required columns
    required_cols = {"transaction_id", "sender_id", "receiver_id", "amount", "timestamp"}
    csv_cols = set(df.columns)
    missing = required_cols - csv_cols

    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid CSV format. Missing columns: {', '.join(missing)}. "
                   f"Found columns: {list(df.columns)}"
        )

    # 7. Convert to records
    transactions = df.to_dict(orient="records")

    # 8. Build graph
    graph = build_graph(transactions)

    # 9. Pre-filter graph for performance
    active_nodes = [n for n in graph.nodes() if graph.degree(n) > 1]
    subgraph = graph.subgraph(active_nodes)

    # 10. Run detectors (optimized)
    rings = []
    rings.extend(detect_cycles(subgraph))
    rings.extend(detect_smurfing(transactions))
    rings.extend(detect_shell_networks(subgraph))

    # 11. Compute scores
    suspicious_accounts, fraud_rings = compute_scores(rings)

    # 12. Build response
    response = build_response(
        suspicious_accounts=suspicious_accounts,
        fraud_rings=fraud_rings,
        total_accounts=len(graph.nodes),
        processing_time=0.0  # you can add real timing later
    )

    return response
