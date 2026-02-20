# detectors/cycles.py

import networkx as nx


def detect_cycles(graph):
    """
    Scalable cycle detection using Strongly Connected Components (SCC).
    This replaces expensive nx.simple_cycles() which crashes on 10K+ edges.
    """

    rings = []
    ring_id = 1

    # Strongly Connected Components (O(V + E))
    scc_components = list(nx.strongly_connected_components(graph))

    for component in scc_components:
        size = len(component)

        # Only treat meaningful cycles (3–10 nodes)
        if 3 <= size <= 10:
            rings.append({
                "ring_id": f"RING_{ring_id:03d}",
                "member_accounts": list(component),
                "pattern_type": "cycle"
            })
            ring_id += 1

    return rings
