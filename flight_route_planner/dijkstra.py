from typing import List, Dict, Set, Tuple
from dataclasses import dataclass
from flight_route_planner import graphs


# @dataclass is an annotation that automatically generates
# __init__, __repr__ and __eq__ methods for VertexPath
@dataclass
class VertexPath:
    """Data structure that is used to save information about current vertex
    to implement dijkstra algorithm.

    Attributes:
        shortest_distance: An integer representing the shortest distance from
        the start vertex to the current vertex.
        previous_vertex: An integer representing previous vertex.
    """

    shortest_distance: float
    previous_vertex: graphs.Vertex


def find_shortest_path(
    graph: graphs.Graph, start_vertex: graphs.Vertex, end_vertex: graphs.Vertex
) -> List[graphs.Vertex]:
    """Implements dijkstra algorithm that finds the shortest path between two
    vertices in a graph.

    Args:
        graph: An instance of a class Graph in a form of a table of integers.
        start_vertex: An integer that represents the start vertex.
        end_vertex: An integer that represents the end vertex.

    Returns:
        start_to_end_path: A list of integers representing a list of vertices or
        a shortest path from the start vertex to the end vertex.
    """

    dijkstra_path_table: Dict[graphs.Vertex, VertexPath] = {}
    # using set instead of list for O(1=const) look-up complexity
    # (list is O(n=number of elements)); set has no duplicate elements
    unvisited_vertices: Set[graphs.Vertex] = set(graph.vertices())

    dijkstra_path_table[start_vertex] = VertexPath(
        shortest_distance=0, previous_vertex=start_vertex
    )

    while len(unvisited_vertices) > 0:
        current_vertex, current_distance = find_unvisited_vertex_closest_to_start(
            unvisited_vertices, dijkstra_path_table
        )

        unvisited_neighbors = find_unvisited_neighbors(
            graph, current_vertex, unvisited_vertices
        )

        # calculate distance of each unvisited neighbor from the start
        for neighbor in unvisited_neighbors:
            distance_to_neighbor = graph.edge_weight(current_vertex, neighbor)
            new_shortest_distance_to_neighbor = current_distance + distance_to_neighbor

            # if the known shortest distance to neighbor is less than new distance,
            # don't update the neighbor
            if (
                neighbor in dijkstra_path_table
                and dijkstra_path_table[neighbor].shortest_distance
                <= new_shortest_distance_to_neighbor
            ):
                continue

            # otherwise update the table with new shortest distance
            # to the neighbor from the start vertex
            dijkstra_path_table[neighbor] = VertexPath(
                new_shortest_distance_to_neighbor, previous_vertex=current_vertex
            )

    return reconstruct_shortest_path(dijkstra_path_table, start_vertex, end_vertex)


def find_unvisited_vertex_closest_to_start(
    unvisited_vertices: Set[graphs.Vertex],
    dijkstra_path_table: Dict[graphs.Vertex, VertexPath],
) -> Tuple[graphs.Vertex, float]:
    """Finds unvisited vertex with shortest distance to the start vertex.

    Args:
        unvisited_vertices:  A set of unvisited vertices initially filled with
        all vertices.
        dijkstra_path_table: A dictionary includes vertex (integer) as its key
        and data structure VertexPath described above as its value.

    Returns:
        A tuple consists of found unvisited vertex (integer) with shortest
        distance to the start vertex and its shortest distance.

    Raises:
        AssertionError
    """
    # sort vertices by shortest distance in dictionary
    sorted_vertices = sorted(
        dijkstra_path_table, key=lambda k: dijkstra_path_table[k].shortest_distance
    )

    for vertex in sorted_vertices:
        if vertex in unvisited_vertices:
            unvisited_vertices.remove(vertex)
            return vertex, dijkstra_path_table[vertex].shortest_distance

    raise AssertionError("Failed to find closest vertex.")


def find_unvisited_neighbors(
    graph: graphs.Graph, vertex: graphs.Vertex, unvisited_vertices: Set[graphs.Vertex]
) -> List[graphs.Vertex]:
    return [
        neighbor
        for neighbor in graph.find_neighbors(vertex)
        if neighbor in unvisited_vertices
    ]


def reconstruct_shortest_path(
    dijkstra_path_table: Dict[graphs.Vertex, VertexPath],
    start_vertex: graphs.Vertex,
    end_vertex: graphs.Vertex,
) -> List[graphs.Vertex]:
    end_to_start_path = [end_vertex]

    # starting from the end vertex reconstruct the path to the start vertex
    while end_to_start_path[-1] != start_vertex:
        last_vertex = end_to_start_path[-1]
        previous_vertex = dijkstra_path_table[last_vertex].previous_vertex

        end_to_start_path.append(previous_vertex)

    start_to_end_path = end_to_start_path[::-1]

    return start_to_end_path
