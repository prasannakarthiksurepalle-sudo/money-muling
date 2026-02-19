def build_response(suspicious_accounts, fraud_rings, total_accounts, processing_time):
    return {
        "suspicious_accounts": suspicious_accounts,
        "fraud_rings": fraud_rings,
        "summary": {
            "total_accounts_analyzed": total_accounts,
            "suspicious_accounts_flagged": len(suspicious_accounts),
            "fraud_rings_detected": len(fraud_rings),
            "processing_time_seconds": processing_time
        }
    }
