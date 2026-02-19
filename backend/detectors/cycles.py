def detect_cycles(graph, max_len=3):
    rings = []
    ring_id = 1

    # Pre-filter nodes with some activity
    candidates = [n for n in graph.nodes() if graph.in_degree(n) + graph.out_degree(n) >= 2]
    sub = graph.subgraph(candidates)

    for a in sub.nodes():
        for b in sub.successors(a):
            for c in sub.successors(b):
                if graph.has_edge(c, a):  # 3-cycle
                    rings.append({
                        "ring_id": f"RING_{ring_id:03d}",
                        "pattern_type": "cycle",
                        "member_accounts": [a, b, c],
                    })
                    ring_id += 1

    return rings
