import requests
from typing import NamedTuple

from exceptions import CantGetCoordinatesError


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates_by_address() -> Coordinates:
    """Returns coordinates using IP-address"""
    try:
        response = requests.get(f"http://ip-api.com/json/")
        data = response.json()
        return Coordinates(latitude=data["lat"], longitude=data["lon"])
    except ConnectionError:
        raise CantGetCoordinatesError
