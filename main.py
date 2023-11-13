from coordinates import get_coordinates_by_address
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import APIServiceError, CantGetCoordinatesError


def main():
    try:
        coordinates = get_coordinates_by_address()
    except CantGetCoordinatesError:
        print("Ошибка при получении координат")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except APIServiceError:
        print("Ошибка при получении погоды")
        exit(1)
    print(format_weather(weather))


if __name__ == "__main__":
    main()