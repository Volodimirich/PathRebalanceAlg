import networkx as nx


class Algorithm():
    def __init__(self, graph, requests):
        print(graph)
        self.graph = graph
        print(self.graph)
        self.back_graph = nx.MultiDiGraph(graph, key='front')
        self.back_edges = set()
        self.req = requests

    def get_list_pairs(self, list):
        it = iter(list)
        old = next(it, None)
        for new in it:
            yield old, new
            old = new

    def graph_mutation(self, path, band):
        iter = self.get_list_pairs(path)
        for i in range(len(path) - 1):
            st, nxt = next(iter)
            print(st, nxt)
            self.graph[st][nxt]['weight'] -= band

            if not self.back_graph.has_edge(nxt, str, key='back'):
                self.back_graph.add_edge(nxt, st, key='back', weight=band)
            else:
                self.back_graph[nxt][st]['back']['weight'] += band

            self.back_graph[st][nxt][0]['weight'] -= band

    def start(self):
        for source, dest, band in self.req:

            if nx.has_path(self.graph, source, dest):
                path = nx.dijkstra_path(self.graph, source, dest)
                self.graph_mutation(path, band)
            else:
                print('@!')

        print('@')
