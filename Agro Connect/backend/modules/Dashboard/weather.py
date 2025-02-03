# Developer: Prajwal Dhage
import requests
from modules.variables import city, weather_api, api_url

def get_city_key():
    """Fetch city key from AccuWeather using the city name."""
    url = f"{api_url}/locations/v1/cities/search?apikey={weather_api}&q={city}"
    response = requests.get(url)
    
    if response.status_code == 200 and response.json():
        return response.json()[0]["Key"]  # Return first matching city key
    return None

def get_weather_data():
    """Fetch full weather data from AccuWeather API."""
    city_key = get_city_key()
    if not city_key:
        return {"error": "City not found"}

    url = f"{api_url}/currentconditions/v1/{city_key}?apikey={weather_api}&details=true"
    response = requests.get(url)
    
    if response.status_code == 200 and response.json():
        weather = response.json()[0]
        return {
            "temperature": weather["Temperature"]["Metric"]["Value"],  # °C
            "humidity": weather["RelativeHumidity"],  # %
            "wind_speed": weather["Wind"]["Speed"]["Metric"]["Value"],  # km/h
            "feels_like": weather["RealFeelTemperature"]["Metric"]["Value"]  # Feels like °C
        }
    return {"error": "Failed to fetch weather data"}
