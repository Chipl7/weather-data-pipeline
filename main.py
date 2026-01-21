import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

URL = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"

TEST_URL = "http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code},{state code},{country code}&limit={limit}&appid={API key}"


def main():
    city = input("В каком городе хотите посмотреть погоду: ")
    req = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
    )
    data = req.json()
    city_info = data[0]
    print(f"Страна {city_info['country']}")
    print(f"Город {city_info['name']}")
    print(f"Широта {city_info['lat']}")
    print(f"Долгота {city_info['lon']}")


if __name__ == "__main__":
    main()
