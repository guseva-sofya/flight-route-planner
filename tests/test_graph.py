from flight_route_planner import graphs
from typing import List


def test_find_vertex_neighbors():
    graph: graphs.Graph = graphs.Graph(num_vertices=4)

    graph.add_edge(vertex1=0, vertex2=1, weight=7)
    graph.add_edge(vertex1=0, vertex2=2, weight=1)
    graph.add_edge(vertex1=1, vertex2=3, weight=3)
    graph.add_edge(vertex1=2, vertex2=3, weight=2)

    neighbors = graph.find_neighbors(1)

    assert neighbors == [0, 3]
