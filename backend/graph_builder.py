import networkx as nx

def build_graph(transactions):
    G = nx.DiGraph()

    for tx in transactions:
        sender = tx["sender_id"]
        receiver = tx["receiver_id"]
        amount = float(tx["amount"])
        timestamp = tx["timestamp"]

        G.add_node(sender)
        G.add_node(receiver)
        G.add_edge(sender, receiver, amount=amount, timestamp=timestamp)

    return G
