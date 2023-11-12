from geopy.geocoders import Nominatim
from typing import NamedTuple
import time


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


app = Nominatim(user_agent="tutorial")


def get_coordinates_by_address(address) -> Coordinates:
    """Returns coordinates using IP-address"""
    pass

