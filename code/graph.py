import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(G, pos, shortest_path=None):
    """
    Visualizes the graph as a 10x10 matrix, highlighting the shortest path,
    filling in missing indices with transparent grey orbs, and making unused edges more transparent.

    Args:
        G (nx.Graph): The graph to visualize.
        pos (dict): Node positions.
        shortest_path (list, optional): List of nodes in the shortest path.
    """
    plt.figure(figsize=(10, 10))
    
    # Draw transparent grey orbs for missing positions
    occupied_positions = set(pos.values())
    all_positions = {(x, y) for x in range(10) for y in range(10)}
    missing_positions = all_positions - occupied_positions
    
    for x, y in missing_positions:
        plt.scatter(x, y, color='lightgrey', alpha=0.3, s=400)  # Small faded grey orbs

    # Draw nodes
    node_colors = ['green' if node == 'start' else 'red' if node == 'end' else 'skyblue' for node in G.nodes()]
    node_sizes = [1000 if node in ['start', 'end'] else 700 for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

    # Distinguish edges visually
    path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path) - 1)] if shortest_path else []
    faded_edges = [edge for edge in G.edges() if edge not in path_edges]

    # Draw edges
    nx.draw_networkx_edges(G, pos, edgelist=faded_edges, edge_color='gray', width=1, alpha=0.5)  # Faded non-path edges
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)  # Bold red path edges

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    faded_labels = {edge: weight for edge, weight in edge_labels.items() if edge not in path_edges}
    path_labels = {edge: weight for edge, weight in edge_labels.items() if edge in path_edges}
    
    # Less visible weights for non-path edges
    nx.draw_networkx_edge_labels(G, pos, edge_labels=faded_labels, font_color='gray', alpha=0.5, font_size=7)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=path_labels, font_color='darkgreen', font_size=8)

    # Styling for 10x10 grid
    plt.title("Jump on crocodiles or die!")
    plt.xlim(-1, 10)
    plt.ylim(-1, 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.xticks(range(10))
    plt.yticks(range(10))
    plt.show()

def read_graph_from_file(filepath):
    """
    Reads graph data from a file, ensuring nodes are placed on a 10x10 grid.
    Locks start node at (0,0) and end node at (9,9), ignoring any changes.

    Args:
        filepath (str): Path to the input file.

    Returns:
        G (nx.Graph): Constructed graph.
        pos (dict): Node positions.
    """
    G = nx.Graph()
    pos = {}

    with open(filepath, 'r') as file:
        section = None
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                if 'NODE' in line:
                    section = 'nodes'
                elif 'EDGE' in line:
                    section = 'edges'
                continue

            if section == 'nodes':
                node_id, x, y = line.split()
                x, y = int(x), int(y)

                # **Force start and end positions to be locked**
                if node_id == 'start':
                    pos[node_id] = (0, 0)
                elif node_id == 'end':
                    pos[node_id] = (9, 9)
                else:
                    if not (0 <= x < 10 and 0 <= y < 10):
                        raise ValueError(f"Node {node_id} position ({x},{y}) is out of bounds.")
                    pos[node_id] = (x, y)

                G.add_node(node_id)

            elif section == 'edges':
                node1, node2, weight = line.split()
                weight = float(weight)
                G.add_edge(node1, node2, weight=weight)

    return G, pos