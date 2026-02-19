def detect_shell_networks(graph):
    rings = []
    ring_id = 200

    for b in graph.nodes():
        if graph.degree(b) <= 3:
            for a in graph.predecessors(b):
                for c in graph.successors(b):
                    if graph.degree(c) <= 3:
                        for d in graph.successors(c):
                            rings.append({
                                "ring_id": f"RING_{ring_id:03d}",
                                "pattern_type": "shell_network",
                                "member_accounts": [a, b, c, d],
                            })
                            ring_id += 1

    return rings
