import os
import requests
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv

# Ensure .env is loaded even if it contains a UTF-8 BOM (common on Windows editors)
load_dotenv(encoding="utf-8-sig")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@dataclass
class WeatherDto:
    temperature: float
    description: str

    @classmethod
    def parse(cls, data: dict) -> 'WeatherDto':
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return cls(temperature=temp, description=desc)


def _get_api_key(existing_key: str | None) -> str:
    if existing_key:
        return existing_key
    env_api_key = os.getenv("OPENWEATHER_API_KEY")
    if env_api_key:
        return env_api_key
    raise ValueError("API key must be provided either as a parameter or via the OPENWEATHER_API_KEY environment variable.")

def get_weather(city: str, existing_key: str | None = None) -> dict:
    api_key = _get_api_key(existing_key)
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        if response.status_code == 404:
            raise ValueError(f"City '{city}' not found.")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching weather data for city: {city} ({e})")


if __name__ == "__main__":
    city_name = input("Enter city name: ").strip()
    try:
        weather_data = get_weather(city_name)
        weather = WeatherDto.parse(weather_data)
        print(f"Current weather in {city_name}: {weather.temperature}°C, {weather.description}")
    except Exception as e:
        print(e)