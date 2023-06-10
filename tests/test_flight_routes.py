import json
from flight_route_planner import flight_routes


def test_find_shortest_flight_route() -> None:
    airports = [
        flight_routes.Airport("LHR", "London Heathrow Airport"),
        flight_routes.Airport("CDG", "Paris Charles de Gaulle Airport"),
        flight_routes.Airport("FRA", "Frankfurt Airport"),
        flight_routes.Airport("FCO", "Rome-Fiumicino Airport"),
    ]

    flights = [
        flight_routes.Flight("LHR", "CDG", 3),
        flight_routes.Flight("LHR", "FRA", 2),
        flight_routes.Flight("FRA", "CDG", 1),
        flight_routes.Flight("FRA", "FCO", 1),
        flight_routes.Flight("CDG", "FCO", 2),
    ]

    fastest_route = flight_routes.find_fastest_flight_route(
        airports, flights, "LHR", "FCO"
    )

    assert ["LHR", "FRA", "FCO"] == fastest_route.airport_codes
    assert 3.0 == fastest_route.total_duration_in_hours


def test_enumerate_airports() -> None:
    airports = [
        flight_routes.Airport("LHR", "London Heathrow Airport"),
        flight_routes.Airport("CDG", "Paris Charles de Gaulle Airport"),
        flight_routes.Airport("FRA", "Frankfurt Airport"),
    ]

    airports_to_vertices = flight_routes.enumerate_airports(airports)

    assert {"CDG": 0, "FRA": 1, "LHR": 2} == airports_to_vertices
