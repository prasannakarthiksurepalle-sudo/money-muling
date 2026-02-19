import networkx as nx

def detect_cycles(graph, min_len=3, max_len=5):
    rings = []
    ring_id = 1

    for cycle in nx.simple_cycles(graph):
        if min_len <= len(cycle) <= max_len:
            rings.append({
                "ring_id": f"RING_{ring_id:03d}",
                "pattern_type": "cycle",
                "member_accounts": cycle,
            })
            ring_id += 1

    return rings
