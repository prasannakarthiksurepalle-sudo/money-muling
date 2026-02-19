from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd

from graph_builder import build_graph
from detectors.cycles import detect_cycles
from detectors.smurfing import detect_smurfing
from detectors.shell_networks import detect_shell_networks
from scoring import compute_scores
from schema import build_response

router = APIRouter()

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")
    try:
        df = pd.read_csv(file.file)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid or empty CSV file")


    required_cols = {"transaction_id", "sender_id", "receiver_id", "amount", "timestamp"}
    if not required_cols.issubset(set(df.columns)):
        raise HTTPException(status_code=400, detail="Invalid CSV format")

    transactions = df.to_dict(orient="records")
    graph = build_graph(transactions)

    rings = []
    rings.extend(detect_cycles(graph))
    rings.extend(detect_smurfing(transactions))
    rings.extend(detect_shell_networks(graph))

    suspicious_accounts, fraud_rings = compute_scores(rings)

    response = build_response(
        suspicious_accounts=suspicious_accounts,
        fraud_rings=fraud_rings,
        total_accounts=len(graph.nodes),
        processing_time=1.2  # mock for now
    )

    return response
