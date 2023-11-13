import urllib.request
import json
from typing import NamedTuple
from urllib.error import URLError
from exceptions import CantGetCoordinatesError


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates_by_address() -> Coordinates:
    """Returns coordinates using IP-address"""
    try:
        response = urllib.request.urlopen("http://ip-api.com/json/")
        data = json.loads(response.read())
        return Coordinates(latitude=data["lat"], longitude=data["lon"])
    except URLError:
        raise CantGetCoordinatesError
