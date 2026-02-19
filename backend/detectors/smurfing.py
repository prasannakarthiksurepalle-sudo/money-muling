def detect_smurfing(transactions, threshold=10):
    rings = []
    ring_id = 100

    sender_map = {}
    receiver_map = {}

    for tx in transactions:
        sender_map.setdefault(tx["sender_id"], []).append(tx)
        receiver_map.setdefault(tx["receiver_id"], []).append(tx)

    for receiver, txs in receiver_map.items():
        if len(txs) >= threshold:
            members = list(set(tx["sender_id"] for tx in txs)) + [receiver]
            rings.append({
                "ring_id": f"RING_{ring_id:03d}",
                "pattern_type": "fan_in",
                "member_accounts": members,
            })
            ring_id += 1

    for sender, txs in sender_map.items():
        if len(txs) >= threshold:
            members = [sender] + list(set(tx["receiver_id"] for tx in txs))
            rings.append({
                "ring_id": f"RING_{ring_id:03d}",
                "pattern_type": "fan_out",
                "member_accounts": members,
            })
            ring_id += 1

    return rings
