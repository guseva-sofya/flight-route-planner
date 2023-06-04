from dataclasses import dataclass
from typing import List

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
    return Route([], 0)
