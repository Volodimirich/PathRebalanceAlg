import networkx as nx


class GraphGenerator():
    def __init__(self):
        self.graph = None

    def problem_graph(self):
        self.graph = nx.Graph()
        self.graph.add_nodes_from([0, 1, 2, 3])
        self.graph.add_edges_from([(0,1), (1, 2), (2, 3), (0, 3)])
        nx.set_edge_attributes(self.graph, values=3, name='weight')
        return self.graph




