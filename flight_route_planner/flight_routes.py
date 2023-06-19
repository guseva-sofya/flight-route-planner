from dataclasses import dataclass
from typing import List, Dict
from flight_route_planner import graphs, dijkstra

AirportCode = str


@dataclass
class Airport:
    code: AirportCode
    full_name: str


@dataclass
class Flight:
    departure: AirportCode
    destination: AirportCode
    duration_in_hours: float


@dataclass
class Route:
    airport_codes: List[AirportCode]
    total_duration_in_hours: float


def find_fastest_flight_route(
    airports: List[Airport],
    scheduled_flights: List[Flight],
    departure_airport: AirportCode,
    destination_airport: AirportCode,
) -> Route:
    """Finds the fastest flight route between departure and destination
    airports using graph alhorithm (dijkstra).

    Args:
        airports: A list of all airports represented as instances of a class Airport.
        scheduled_flights: A list of all flights represented as instances of a class Flight.
        departure_airport: A departure airport represented as airport code.
        destination_airport: A destination airport represented as airport code.

    Returns:
        An instance of a class Route which includes:
        a) sequence of the airport codes corresponding to the fastest route;
        b) total duration of the fastest route.
        For example:

        Route(airport_codes=['MEX', 'CDG', 'AMS', 'FRA'], total_duration_in_hours=15.5)
    """

    airports_to_vertices = enumerate_airports(airports)
    graph: graphs.Graph = graphs.Graph(num_vertices=len(airports_to_vertices))

    for flight in scheduled_flights:
        vertex1 = airports_to_vertices[flight.departure]
        vertex2 = airports_to_vertices[flight.destination]
        graph.add_edge(vertex1, vertex2, weight=flight.duration_in_hours)

    start_vertex = airports_to_vertices[departure_airport]
    end_vertex = airports_to_vertices[destination_airport]

    start_to_end_path = dijkstra.find_shortest_path(graph, start_vertex, end_vertex)

    vertices_to_airports = reverse_airport_dictionary(airports_to_vertices)

    airport_codes_of_fastest_route = [
        vertices_to_airports[vertex] for vertex in start_to_end_path
    ]

    total_duration_in_hours = route_total_duration_in_hours(graph, start_to_end_path)

    return Route(airport_codes_of_fastest_route, total_duration_in_hours)


def enumerate_airports(airports: List[Airport]) -> Dict[AirportCode, graphs.Vertex]:
    """Converts list of airports into a dictionary where airport codes are set as keys
    and the respective vertices (as integers) are set as values.

    Args:
        airports: A list of all airports represented as instances of a class Airport.

    Returns:
        airports_to_vertices: A dictionary with the airport codes sorted in
        alphabetical order set as keys and the respective vertices set as values.
    """

    airports_to_vertices: Dict[AirportCode, graphs.Vertex] = {}
    airport_codes = [airport.code for airport in airports]
    # remove duplicates from a list: list -> set
    sorted_unique_airport_codes = sorted(list(set(airport_codes)))

    for index, airport_code in enumerate(sorted_unique_airport_codes):
        airports_to_vertices[airport_code] = index
    return airports_to_vertices


def reverse_airport_dictionary(
    airports_to_vertices: Dict[AirportCode, graphs.Vertex]
) -> Dict[graphs.Vertex, AirportCode]:
    """Reverses the dictionary with airport codes set as keys and the respective
    vertices set as their values in a way that the verticies become keys and
    the airport codes become values.

    Args:
        airports_to_vertices: A dictionary with airport codes set as keys and
        the respective vertices set as their values.

    Returns:
        vertices_to_airports: A reversed dictionary with vertices set as keys
        and the airport codes set as values.
    """

    vertices_to_airports = {
        vertex: airport_code for airport_code, vertex in airports_to_vertices.items()
    }
    return vertices_to_airports


def route_total_duration_in_hours(
    graph: graphs.Graph, start_to_end_path: List[graphs.Vertex]
) -> float:
    """Calculates the total duration of the fastest route between departure and
    destination airports (converted to vertices).

    Args:
        graph: An instance of a class Graph.
        start_to_end_path: A list of the vertices that represent the fastest route
        between start and end vertices (departure and destination airports).

    Returns:
        total_duration_in_hours: A float which represent the total duration of
        the fastest route in hours.
    """

    length_vertex_list = len(start_to_end_path)
    total_duration_in_hours = 0.0

    for index in range(length_vertex_list - 1):
        vertex1 = start_to_end_path[index]
        vertex2 = start_to_end_path[index + 1]

        duration_in_hours = graph.edge_weight(vertex1, vertex2)
        total_duration_in_hours = total_duration_in_hours + duration_in_hours

    return total_duration_in_hours
