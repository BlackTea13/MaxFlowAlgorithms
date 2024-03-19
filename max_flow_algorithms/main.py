import copy

from graph_def import ResidualGraph
from ford_fulkerson.ford_fulkerson import FordFulkerson
from edmonds_karp.edmonds_karp import EdmondsKarp
from dinics.dinics import Dinic

if __name__ == '__main__':
    print("Hello World!")

g = ResidualGraph(11)
g.add_edge(g.source, 0, 7)
g.add_edge(g.source, 1, 2)
g.add_edge(g.source, 2, 1)

g.add_edge(0, 3, 2)
g.add_edge(0, 4, 4)
g.add_edge(1, 4, 5)
g.add_edge(1, 5, 6)
g.add_edge(2, 3, 4)
g.add_edge(2, 7, 8)

g.add_edge(3, 6, 7)
g.add_edge(3, 7, 1)
g.add_edge(4, 6, 3)
g.add_edge(4, 8, 3)
g.add_edge(4, 5, 8)
g.add_edge(5, 8, 3)

g.add_edge(6, g.sink, 1)
g.add_edge(7, g.sink, 3)
g.add_edge(8, g.sink, 4)

g1 = copy.deepcopy(g)
ff_solver = FordFulkerson()
max_flow = ff_solver.max_flow(graph=g1)

g2 = copy.deepcopy(g)
ek_solver = EdmondsKarp()
max_flow2 = ek_solver.max_flow(graph=g2)

g3 = copy.deepcopy(g)
di_solver = Dinic()
max_flow3 = di_solver.max_flow(graph=g3)

print(max_flow)
print(max_flow2)
print(max_flow3)