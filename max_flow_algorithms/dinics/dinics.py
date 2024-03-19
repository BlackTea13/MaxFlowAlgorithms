import sys
from typing import List, Set, Tuple
from max_flow_algorithms.graph_def import ResidualGraph, Edge


class Dinic:
    def __dfs__(self, graph: ResidualGraph, vertex: int, level: List[int], next: List[int], flow: int) -> int:
        if vertex == graph.sink: return flow
        print(vertex)
        num_nbrs = len(graph.graph[vertex])
        for _ in range(next[vertex], num_nbrs):
            edge = graph.graph[vertex][next[vertex]]
            if edge.remaining_capacity() > 0 and level[edge.end] == level[vertex] + 1:
                bottleneck = self.__dfs__(graph, edge.end, level, next, min(flow, edge.remaining_capacity()))
                if bottleneck > 0:
                    edge.augment_flow(bottleneck)
                    return bottleneck
            next[vertex] += 1
        return 0


    def __bfs__(self, graph: ResidualGraph) -> Tuple[List[int], bool]:
        level = [-1] * graph.num_vertices
        frontier = [graph.source]

        while len(frontier) > 0:
            vertex = frontier.pop(0)
            if vertex == graph.sink: break

            neighbors = graph.graph[vertex]
            for edge in neighbors:
                if edge.remaining_capacity() > 0 and level[edge.end] == -1:
                    level[edge.end] = level[vertex] + 1
                    frontier.append(edge.end)

        return level, level[graph.sink] != -1

    def max_flow(self, graph:ResidualGraph) -> int:
        inf = sys.maxsize
        max_f = 0
        level, sink_reachable = self.__bfs__(graph)
        while sink_reachable:
            next = [0] * graph.num_vertices
            flow = self.__dfs__(graph, graph.source, level, next, inf)
            while flow != 0:
                max_f += flow
                flow = self.__dfs__(graph, graph.source, level, next, inf)
        return max_f




