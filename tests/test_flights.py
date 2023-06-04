from flight_route_planner import flights, graphs, dijkstra
from tests import test_graph


def test_find_shortest_flight_route() -> None:
    airports = [
        flights.Airport("LHR", "London Heathrow Airport"),
        flights.Airport("CDG", "Paris Charles de Gaulle Airport"),
        flights.Airport("FRA", "Frankfurt Airport"),
    ]

    scheduled_flights = [
        flights.Flight("LHR", "CDG", 3),
        flights.Flight("LHR", "FRA", 1.5),
        flights.Flight("FRA", "CDG", 1),
    ]

    fastest_route = flights.find_fastest_flight_route(airports, scheduled_flights)

    assert ["LHR", "FRA", "CDG"] == fastest_route.airport_codes
    assert 2.5 == fastest_route.total_duration_in_hours
