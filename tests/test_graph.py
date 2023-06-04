from typing import List
from flight_route_planner import graphs


def test_find_vertex_neighbors() -> None:
    graph: graphs.Graph = create_test_graph()

    neighbors: List[graphs.Vertex] = graph.find_neighbors(1)

    assert [0, 3] == neighbors


def test_get_all_vertices() -> None:
    graph: graphs.Graph = create_test_graph()

    all_vertices: List[graphs.Vertex] = graph.vertices()

    assert [0, 1, 2, 3] == all_vertices


def test_get_edge_weight_between_vertices() -> None:
    graph: graphs.Graph = create_test_graph()

    weight: float = graph.edge_weight(vertex1=0, vertex2=1)

    assert 7 == weight


def create_test_graph() -> graphs.Graph:
    graph: graphs.Graph = graphs.Graph(num_vertices=4)

    graph.add_edge(vertex1=0, vertex2=1, weight=7.0)
    graph.add_edge(vertex1=0, vertex2=2, weight=1.0)
    graph.add_edge(vertex1=1, vertex2=3, weight=3.0)
    graph.add_edge(vertex1=2, vertex2=3, weight=2.0)

    return graph
