from flight_route_planner import graphs, dijkstra


def test_find_shortest_path():
    graph: graphs.Graph = graphs.Graph(num_vertices=4)

    graph.add_edge(vertex1=0, vertex2=1, weight=7)
    graph.add_edge(vertex1=0, vertex2=2, weight=1)
    graph.add_edge(vertex1=1, vertex2=3, weight=3)
    graph.add_edge(vertex1=2, vertex2=3, weight=2)

    shortest_path = dijkstra.find_shortest_path(graph, start_vertex=0, end_vertex=3)

    assert [0, 2, 3] == shortest_path
