import os
import json
from typing import Any, Callable, Dict, List
from flight_route_planner import flight_routes


def main():
    airports = load_airports()
    flights = load_flights()
    for airport in airports:
        print(airport)

    for flight in flights:
        print(flight)


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
