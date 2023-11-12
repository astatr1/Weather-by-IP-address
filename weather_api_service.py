from datetime import datetime
from typing import NamedTuple
from enum import Enum

from coordinates import Coordinates


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
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLOUDS,
        sunrise=datetime.fromisoformat("2020-05-04T04:00:00"),
        sunset=datetime.fromisoformat("2020-05-04T20:35:00"),
        city="Saint-Petersburg"
    )