import dijkstra as dj
import graph as g

if __name__ == '__main__':
    filepath = "graph.txt"
    G, pos = g.read_graph_from_file(filepath)

    shortest_path = dj.find_shortest_path(G, 'start', 'end')
    g.visualize_graph(G, pos, shortest_path)
