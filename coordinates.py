import requests
from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates_by_address() -> Coordinates:
    """Returns coordinates using IP-address"""
    try:
        response = requests.get(f"http://ip-api.com/json/")
        data = response.json()
        return Coordinates(latitude=data["lat"], longitude=data["lon"])
    except requests.ConnectionError as e:
        print("OOPS! Connection Error. Make sure you are connected to Internet")
    except requests.Timeout as e:
        print("OOPS! Timeout Error")
    except requests.RequestException as e:
        print("OOPS! Request Error")