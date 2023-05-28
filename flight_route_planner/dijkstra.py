from flight_route_planner import graphs
from typing import List, Dict, Set
from dataclasses import dataclass


# @dataclass is an annotation that automatically generates
# __init__, __repr__ and __eq__ methods for VertexPath
@dataclass
class VertexPath:
    shortest_distance: int
    previous_vertex: graphs.Vertex


def find_shortest_path(
    graph: graphs.Graph, start_vertex: graphs.Vertex, end_vertex: graphs.Vertex
) -> List[graphs.Vertex]:
    dijkstra_path_table: Dict[graphs.Vertex, VertexPath] = {}
    # using set instead of list for O(1=const) look-up complexity
    # (list is O(n=number of elements)); set has no duplicate elements
    unvisited_vertices: Set[graphs.Vertex] = set(graph.vertices())

    dijkstra_path_table[start_vertex] = VertexPath(
        shortest_distance=0, previous_vertex=start_vertex
    )

    while len(unvisited_vertices) > 0:
        current_vertex = find_unvisited_vertex_closest_to_start(
            unvisited_vertices, dijkstra_path_table
        )
        unvisited_vertices.remove(current_vertex)

        # find unvisited neighbors of current vertex
        unvisited_neighbors = [
            neighbor
            for neighbor in graph.find_neighbors(current_vertex)
            if neighbor in unvisited_vertices
        ]

        # calculate distance of each unvisted neighbor from the start
        for neighbor in unvisited_neighbors:
            current_vertex_distance = dijkstra_path_table[
                current_vertex
            ].shortest_distance

            distance_to_neighbor = graph.edge_weight(current_vertex, neighbor)

            new_shortest_distance_to_neighbor = (
                current_vertex_distance + distance_to_neighbor
            )

            # if the calculated distance of neighbor is less than known distance,
            # update the shortest distance. if neighbor is not in the table, adding it
            if neighbor in dijkstra_path_table:
                shortest_distance_to_neighbor = dijkstra_path_table[
                    neighbor
                ].shortest_distance

                if new_shortest_distance_to_neighbor < shortest_distance_to_neighbor:
                    dijkstra_path_table[neighbor] = VertexPath(
                        new_shortest_distance_to_neighbor,
                        previous_vertex=current_vertex,
                    )
            else:
                dijkstra_path_table[neighbor] = VertexPath(
                    new_shortest_distance_to_neighbor, previous_vertex=current_vertex
                )

    return reconstruct_shortest_path(dijkstra_path_table, start_vertex, end_vertex)


def find_unvisited_vertex_closest_to_start(
    unvisited_vertices: Set[graphs.Vertex],
    dijkstra_path_table: Dict[graphs.Vertex, VertexPath],
) -> graphs.Vertex:
    # sort vertices by shortest distance in dictionary
    sorted_vertices = sorted(
        dijkstra_path_table, key=lambda k: dijkstra_path_table[k].shortest_distance
    )

    for vertex in sorted_vertices:
        if vertex in unvisited_vertices:
            return vertex

    raise Exception("Failed to find closest vertex.")


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

    end_to_start_path.reverse()

    return end_to_start_path
