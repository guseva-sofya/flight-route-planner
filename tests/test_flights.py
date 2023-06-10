import json
from flight_route_planner import flights


def test_find_shortest_flight_route() -> None:
    airports = [
        flights.Airport("LHR", "London Heathrow Airport"),
        flights.Airport("CDG", "Paris Charles de Gaulle Airport"),
        flights.Airport("FRA", "Frankfurt Airport"),
        flights.Airport("FCO", "Rome-Fiumicino Airport"),
    ]

    scheduled_flights = [
        flights.Flight("LHR", "CDG", 3),
        flights.Flight("LHR", "FRA", 2),
        flights.Flight("FRA", "CDG", 1),
        flights.Flight("FRA", "FCO", 1),
        flights.Flight("CDG", "FCO", 2),
    ]

    fastest_route = flights.find_fastest_flight_route(
        airports, scheduled_flights, "LHR", "FCO"
    )

    assert ["LHR", "FRA", "FCO"] == fastest_route.airport_codes
    assert 3.0 == fastest_route.total_duration_in_hours


def test_enumerate_airports() -> None:
    airports = [
        flights.Airport("LHR", "London Heathrow Airport"),
        flights.Airport("CDG", "Paris Charles de Gaulle Airport"),
        flights.Airport("FRA", "Frankfurt Airport"),
    ]

    airports_to_vertices = flights.enumerate_airports(airports)

    assert {"CDG": 0, "FRA": 1, "LHR": 2} == airports_to_vertices
