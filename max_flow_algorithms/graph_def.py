from typing import List, Dict
from collections import defaultdict

class Edge:
    """
    A class representing directed edges between two vertices. In a residual graph, this
    edge contains a capacity and a flow value.
    """
    def __init__(self, start: int, end: int, capacity: int):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.residual_edge = None

    def __repr__(self):
        return f"Edge(start={self.start}, end={self.end}, capacity={self.capacity}, flow={self.flow})"

    def remaining_capacity(self) -> int:
        return self.capacity - self.flow

    def augment_flow(self, bottleneck: int) -> None:
        self.flow += bottleneck
        self.residual_edge.flow -= bottleneck

class ResidualGraph:
    """
    A class representing a residual graph.
    """
    source: int
    sink: int
    num_vertices: int
    graph: Dict[int, List[Edge]]

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.source = self.num_vertices - 2
        self.sink = self.num_vertices - 1
        self.vertexes = [i for i in range(self.num_vertices - 2)]
        self.edges = []
        self.graph = defaultdict(list[Edge])

    def add_edge(self, source: int, destination: int, capacity: int, flow: int = 0):
        edge = Edge(source, destination, capacity)
        edge.residual_edge = Edge(destination, source, 0)
        edge.residual_edge.residual_edge = edge

        self.graph[source].append(edge)
        self.graph[destination].append(edge.residual_edge)

        self.edges.append(edge)
