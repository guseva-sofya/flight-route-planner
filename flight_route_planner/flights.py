from dataclasses import dataclass
from typing import List, Dict
from flight_route_planner import graphs

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
    airports: List[Airport], scheduled_flights: List[Flight]
) -> Route:
    num_airports = len(airports)
    graph: graphs.Graph = graphs.Graph(num_vertices=num_airports)

    # for flight in scheduled_flights:
    #     graph.add_edge(vertex1=, vertex2=1, weight=7)

    return Route([], 0)


def enumerate_airports(airports: List[Airport]) -> Dict[AirportCode, graphs.Vertex]:
    airports_to_vertices: Dict[AirportCode, graphs.Vertex] = {}
    airport_codes = [airport.code for airport in airports]
    # remove duplicates from a list: list -> set
    sorted_unique_airport_codes = sorted(list(set(airport_codes)))

    for index, airport_code in enumerate(sorted_unique_airport_codes):
        airports_to_vertices[airport_code] = index
    return airports_to_vertices
