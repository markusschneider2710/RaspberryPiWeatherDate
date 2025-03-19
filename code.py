import epd4in2
import time
from PIL import Image, ImageDraw, ImageFont
import board
import adafruit_dht
import requests

# Initialize the e-Paper display
epd = epd4in2.EPD()
epd.init()

# Initialize the DHT11 sensor
dhtDevice = adafruit_dht.DHT11(board.D4)

# OpenWeatherMap API Key
API_KEY = "..."

# Function to read DHT11 sensor data
def read_sensor_data():
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        return temperature_f, temperature_c, humidity
    except RuntimeError as error:
        print(error.args[0])
        return None, None, None
    except Exception as error:
        print(f"Fehler beim Lesen der Sensordaten: {error}")
        return None, None, None

# Function to fetch weather data from OpenWeatherMap
def fetch_weather(city_name):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Wetterdaten: {e}")
        return None

# Function to display weather information
def display_weather_info(weather_data):
    if weather_data:
        print(f"Wetter in {weather_data['name']}:")
        print(f"Temperatur: {weather_data['main']['temp']}°C")
        print(f"Luftfeuchtigkeit: {weather_data['main']['humidity']}%")
        print(f"Beschreibung: {weather_data['weather'][0]['description']}")
    else:
        print("Fehler beim Abrufen der Wetterdaten.")

# Dictionary mapping weather codes to Meteocons characters
weather_icon_dict = {
    '01d': 'B',  # Clear sky
    '02d': 'C',  # Few clouds
    '03d': 'D',  # Scattered clouds
    '04d': 'E',  # Broken clouds
    '09d': 'F',  # Shower rain
    '10d': 'G',  # Rain
    '11d': 'H',  # Thunderstorm
    '13d': 'I',  # Snow
    '50d': 'J',  # Mist
    '01n': 'K',  # Clear sky night
    '02n': 'L',  # Few clouds night
    '03n': 'M',  # Scattered clouds night
    '04n': 'N',  # Broken clouds night
    '09n': 'O',  # Shower rain night
    '10n': 'P',  # Rain night
    '11n': 'Q',  # Thunderstorm night
    '13n': 'R',  # Snow night
    '50n': 'S',  # Mist night
}

# Main loop
while True:
    # Read sensor data
    temperature_f, temperature_c, humidity = read_sensor_data()
    if temperature_f is not None and temperature_c is not None and humidity is not None:
        print(f"Temp: {temperature_c:.1f} °C / {temperature_f:.1f} F    Humidity: {humidity}%")
        
        # Fetch and display weather data
        city_name = "Hamburg"
        weather_data = fetch_weather(city_name)
        display_weather_info(weather_data)

        # Create an image for the e-Paper display (horizontal orientation)
        image = Image.new('1', (epd.width, epd.height), 255)  # Use width first for horizontal orientation
        draw = ImageDraw.Draw(image)

        # Load a font
        font = ImageFont.truetype('/home/desk/font/FuturaCyrillicBook.ttf', 24)
        weather_font = ImageFont.truetype('/home/desk/font/meteocons-font/FONT/Desktop-font/meteocons.ttf', 80)
        exclamation_font = ImageFont.truetype('/home/desk/font/FuturaCyrillicBook.ttf', 48)

        # Draw the current time
        draw.text((10, 10), f"Datum:", font=font, fill=0)
        draw.text((10, 30), f"{time.strftime('%d.%m.%Y')}", font=font, fill=0)
        draw.text((210, 10), f"Uhrzeit:", font=font, fill=0)
        draw.text((210, 30), f"{time.strftime('%H:%M')}", font=font, fill=0)

        # Draw a vertical line to separate date and time
        draw.line((200, 0, 200, 68), fill=0, width=3)

        # Draw a horizontal line below the time
        draw.line((0, 68, epd.width, 68), fill=0, width=3)

        # Draw text horizontally on the image
        draw.text((10, 70), f"Zimmertemperatur:", font=font, fill=0)
        draw.text((10, 95), f"Temp: {temperature_c:.1f} °C / {temperature_f:.1f} F", font=font, fill=0)
        draw.text((10, 120), f"Luftfeuchtigkeit: {humidity}%", font=font, fill=0)

        # Draw a vertical line to separate Temperatur and the explanation mark
        draw.line((250, 68, 250, 153), fill=0, width=3)

        # Check for temperature or humidity thresholds
        if temperature_c > 25 or humidity < 20 or humidity > 60:
        # Draw the exclamation mark next to the temperature text
            draw.text((320, 80), "!", font=exclamation_font, fill=0)

        # Draw a horizontal line below the time
        draw.line((0, 152, epd.width, 152), fill=0, width=3)
     
        if weather_data:
            draw.text((10, 160), f"Wetter in {weather_data['name']}", font=font, fill=0)
            draw.text((10, 185), f"Temperatur: {weather_data['main']['temp']}°C", font=font, fill=0)
            draw.text((10, 210), f"Luftfeuchtigkeit: {weather_data['main']['humidity']}%", font=font, fill=0)
            draw.text((10, 235), f"Beschreibung:", font=font, fill=0)
            draw.text((10, 260), f"{weather_data['weather'][0]['description']}", font=font, fill=0)

            # Draw the weather icon
            weather_code = weather_data['weather'][0]['icon']
            if weather_code in ['01d', '01n']:
                icon_char = 'B' if weather_code == '01d' else 'K'
            elif weather_code in ['02d', '02n']:
                icon_char = 'C' if weather_code == '02d' else 'L'
            elif weather_code in ['03d', '03n']:
                icon_char = 'D' if weather_code == '03d' else 'M'
            elif weather_code in ['04d', '04n']:
                icon_char = 'E' if weather_code == '04d' else 'N'
            elif weather_code in ['09d', '09n']:
                icon_char = 'F' if weather_code == '09d' else 'O'
            elif weather_code in ['10d', '10n']:
                icon_char = 'G' if weather_code == '10d' else 'P'
            elif weather_code in ['11d', '11n']:
                icon_char = 'H' if weather_code == '11d' else 'Q'
            elif weather_code in ['13d', '13n']:
                icon_char = 'I' if weather_code == '13d' else 'R'
            elif weather_code in ['50d', '50n']:
                icon_char = 'J' if weather_code == '50d' else 'S'
            else:
                icon_char = 'X'  # Default icon

            draw.text((250, 190), icon_char, font=weather_font, fill=0)

        # Display the image on the e-Paper without rotation
        epd.display(epd.getbuffer(image))

    # Wait for a bit before updating again
    time.sleep(180)

# De-initialize the e-Paper display
epd.sleep()
