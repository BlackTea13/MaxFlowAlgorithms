import sys
from typing import Set
from max_flow_algorithms.graph_def import ResidualGraph

class FordFulkerson:
    def __dfs__(self, graph: ResidualGraph, vertex: int, flow: int, visited: Set[int]=None) -> int:
        if visited is None:
            visited = set()
        if vertex == graph.sink:
            return flow

        visited.add(vertex)

        neighbors = graph.graph[vertex]
        for edge in neighbors:
            if edge.remaining_capacity() > 0 and edge.end not in visited:
                bottleneck = self.__dfs__(graph, edge.end, min(flow, edge.remaining_capacity()), visited=visited)

                if bottleneck > 0:
                    edge.augment_flow(bottleneck)
                    return bottleneck

        return 0


    def max_flow(self, graph: ResidualGraph) -> int:
        # Find an augmenting path (a path with vertices unused capacity greater than 0)
        inf = sys.maxsize
        source = graph.source
        max_f = 0
        flow = self.__dfs__(graph, source, inf)
        while flow != 0:
            max_f += flow
            flow = self.__dfs__(graph, source, inf)

        return max_f




