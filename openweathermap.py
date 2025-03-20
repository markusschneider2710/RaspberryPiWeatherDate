import requests
import time

# API Key von OpenWeatherMap
API_KEY = "paste in your API-KEY"

def fetch_weather(city_name):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={Hamburg}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(base_url)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Wetterdaten: {e}")
        return None

def display_weather_info(weather_data):
    if weather_data:
        print(f"Wetter in {weather_data['name']}:")
        print(f"Temperatur: {weather_data['main']['temp']}°C")
        print(f"Luftfeuchtigkeit: {weather_data['main']['humidity']}%")
        print(f"Beschreibung: {weather_data['weather'][0]['description']}")
    else:
        print("Fehler beim Abrufen der Wetterdaten.")

def main():
    city_name = "Hamburg"  # city name
    while True:
        weather_data = fetch_weather(city_name)
        display_weather_info(weather_data)
        print(f"Letzte Aktualisierung: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(3600)  # refresh time

if __name__ == "__main__":
    main()
