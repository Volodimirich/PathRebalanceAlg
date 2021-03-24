from GraphGenerator.GraphGenerator import GraphGenerator
from RequestCreator.RequestCreator import RequestCreator
from Algorithm.Algorithm import Algorithm

if __name__ == '__main__':
    graph = GraphGenerator().problem_graph()
    req = RequestCreator().problem_request()
    Algorithm(graph, req).start()


