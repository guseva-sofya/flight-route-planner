from flight_route_planner import graphs, dijkstra
from tests import test_graph


def test_find_shortest_path() -> None:
    graph: graphs.Graph = test_graph.create_test_graph()

    shortest_path = dijkstra.find_shortest_path(graph, start_vertex=0, end_vertex=3)

    assert [0, 2, 3] == shortest_path
