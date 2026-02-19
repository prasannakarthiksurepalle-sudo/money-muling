def compute_scores(rings):
    suspicious_accounts = {}
    fraud_rings = []

    for ring in rings:
        pattern = ring["pattern_type"]

        if pattern == "cycle":
            risk = 90.0
        elif pattern in ["fan_in", "fan_out"]:
            risk = 75.0
        else:
            risk = 85.0

        ring["risk_score"] = risk
        fraud_rings.append(ring)

        for acc in ring["member_accounts"]:
            suspicious_accounts.setdefault(acc, {
                "account_id": acc,
                "suspicion_score": 0,
                "detected_patterns": [],
                "ring_id": ring["ring_id"]
            })

            suspicious_accounts[acc]["suspicion_score"] += risk / 2
            if pattern not in suspicious_accounts[acc]["detected_patterns"]:
                suspicious_accounts[acc]["detected_patterns"].append(pattern)


    result = list(suspicious_accounts.values())
    result.sort(key=lambda x: x["suspicion_score"], reverse=True)

    return result, fraud_rings
