import os
import json
from typing import Any, Callable, Dict, List
from flight_route_planner import flight_routes


def main():
    airports = load_airports()
    flights = load_flights()

    print("Available airports: ")
    for airport in airports:
        print(airport.code, " - ", airport.full_name)

    departure_airport = prompt_airport_code_unit_valid(
        airports, "Enter departure airport code: "
    )
    destination_airport = prompt_airport_code_unit_valid(
        airports, "Enter destination airport code: "
    )

    fastest_route = flight_routes.find_fastest_flight_route(
        airports, flights, departure_airport, destination_airport
    )

    print_fastest_route(fastest_route)


def load_airports() -> List[flight_routes.Airport]:
    def airport_hook(data):
        return flight_routes.Airport(data["code"], data["full_name"])

    airports = load_json_data("flights_data/airports.json", airport_hook)

    return airports


def load_flights() -> List[flight_routes.Flight]:
    def flight_hook(data):
        return flight_routes.Flight(
            data["departure"], data["destination"], data["duration_in_hours"]
        )

    flights = load_json_data("flights_data/flights.json", flight_hook)

    return flights


def prompt_airport_code_unit_valid(
    airports: List[flight_routes.Airport], prompt_text: str
) -> flight_routes.AirportCode:
    airport_codes = [airport.code for airport in airports]
    while True:
        user_input = input(prompt_text)
        if user_input in airport_codes:
            return user_input
        else:
            print("Input value is not a valid airport code!")


def print_fastest_route(fastest_route: flight_routes.Route) -> None:
    print("Shortest route:", " -> ".join(fastest_route.airport_codes))
    print("Total duration:", fastest_route.total_duration_in_hours, "hours")


def load_json_data(
    file_path: str, object_hook: Callable[[Dict[str, Any]], Any]
) -> List[Any]:
    script_directory = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path = os.path.join(script_directory, file_path)
    with open(absolute_file_path, "r") as file:
        json_data = file.read()

    loaded_objects = json.loads(json_data, object_hook=object_hook)

    return loaded_objects


if __name__ == "__main__":
    main()
