import sys
from typing import List
from max_flow_algorithms.graph_def import ResidualGraph, Edge

class EdmondsKarp:
    def __bfs__(self, graph: ResidualGraph) -> int:
        frontier = []
        visited = set()
        frontier.append(graph.source)
        visited.add(graph.source)
        path: List[Edge] = [None] * graph.num_vertices

        while len(frontier) > 0:
            vertex = frontier.pop(0)
            if vertex == graph.sink: break

            neighbors = graph.graph[vertex]
            for edge in neighbors:
                if edge.remaining_capacity() > 0 and edge.end not in visited:
                    visited.add(edge.end)
                    path[edge.end] = edge
                    frontier.append(edge.end)

        if path[graph.sink] is None: return 0

        bottleneck = sys.maxsize
        edge = path[graph.sink]
        while edge is not None:
            bottleneck = min(bottleneck, edge.remaining_capacity())
            edge = path[edge.start]

        edge = path[graph.sink]
        while edge is not None:
            edge.augment_flow(bottleneck)
            edge = path[edge.start]
        return bottleneck

    def max_flow(self, graph: ResidualGraph) -> int:
        max_f = 0
        flow = self.__bfs__(graph)
        while flow != 0:
            max_f += flow
            flow = self.__bfs__(graph)

        return max_f