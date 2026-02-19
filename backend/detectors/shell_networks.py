import networkx as nx

def detect_shell_networks(graph):
    rings = []
    ring_id = 200

    for source in graph.nodes():
        for target in graph.nodes():
            if source == target:
                continue
            try:
                paths = nx.all_simple_paths(graph, source, target, cutoff=4)
                for path in paths:
                    if len(path) >= 3:
                        intermediates = path[1:-1]
                        if all(graph.degree(n) <= 3 for n in intermediates):
                            rings.append({
                                "ring_id": f"RING_{ring_id:03d}",
                                "pattern_type": "shell_network",
                                "member_accounts": path,
                            })
                            ring_id += 1
            except:
                pass

    return rings
