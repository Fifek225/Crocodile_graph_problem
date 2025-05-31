import networkx as nx

def find_shortest_path(G, start, end):
    """
    Finds the shortest path using Dijkstra's algorithm while ignoring edges with weight > 5.

    Args:
        G (nx.Graph): The graph.
        start (str): Start node.
        end (str): End node.

    Returns:
        list: Shortest path nodes, or None if no valid path exists.
    """
    filtered_G = nx.Graph()
    for u, v, d in G.edges(data=True):
        if d['weight'] <= 5:
            filtered_G.add_edge(u, v, weight=d['weight'])

    try:
        return nx.dijkstra_path(filtered_G, source=start, target=end, weight='weight')
    except nx.NetworkXNoPath:
        return None