import json
import ssl
import urllib
from datetime import datetime
from json import JSONDecodeError
from typing import NamedTuple, Literal
from enum import Enum
from urllib.error import URLError

import config
from coordinates import Coordinates
from exceptions import APIServiceError

Celsius = int


class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Мелкий дождь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    """Request weather in OpenWeather API and return it"""
    openweather_responce = _get_openweather_response(
        longitude=coordinates.longitude, latitude=coordinates.latitude)
    weather = _parse_openweather_response(openweather_responce)
    return weather


def _get_openweather_response(latitude: float, longitude: float) -> str:
    ssl.create_default_https_context = ssl._create_unverified_context
    url = config.OPENWEATHER_URL.format(lat=latitude, lon=longitude)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise APIServiceError


def _parse_openweather_response(openweather_responce: str) -> Weather:
    try:
        openweather_dict = json.loads(openweather_responce)
    except JSONDecodeError:
        raise APIServiceError
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict,"sunrise"),
        sunset=_parse_sun_time(openweather_dict, "sunset"),
        city=_parse_city(openweather_dict),
    )


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return openweather_dict["main"]["temp"]


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except(IndexError, KeyError):
        raise APIServiceError
    weather_types ={
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS,
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise APIServiceError


def _parse_sun_time(openweather_dict: dict,
                    time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])


def _parse_city(openweather_dict: dict) -> str:
    return openweather_dict["name"]