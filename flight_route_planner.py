import os
import json
from typing import List
from flight_route_planner import flights


def main():
    airports = load_airports()
    loaded_flights = load_flights()
    for airport in airports:
        print(airport)

    for flight in loaded_flights:
        print(flight)


def load_airports() -> List[flights.Airport]:
    script_directory = os.path.dirname(os.path.abspath(__file__))
    relative_airport_file_path = "flights_data/airports.json"
    absolute_airport_file_path = os.path.join(
        script_directory, relative_airport_file_path
    )
    with open(absolute_airport_file_path, "r") as file:
        json_data = file.read()

    def airport_hook(data):
        return flights.Airport(data["code"], data["full_name"])

    airports = json.loads(json_data, object_hook=airport_hook)

    return airports


def load_flights() -> List[flights.Flight]:
    script_directory = os.path.dirname(os.path.abspath(__file__))
    relative_flight_file_path = "flights_data/flights.json"
    absolute_flight_file_path = os.path.join(
        script_directory, relative_flight_file_path
    )
    with open(absolute_flight_file_path, "r") as file:
        json_data = file.read()

    def flight_hook(data):
        return flights.Flight(
            data["departure"], data["destination"], data["duration_in_hours"]
        )

    loaded_flights = json.loads(json_data, object_hook=flight_hook)

    return loaded_flights


if __name__ == "__main__":
    main()
