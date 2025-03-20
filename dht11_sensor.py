import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D17)

TEMPERATUR_SCHWELLE = 25  
FEUCHTIGKEIT_SCHWELLE = 60  

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

def main():
    while True:
        temperature_f, temperature_c, humidity = read_sensor_data()
        if temperature_f is not None and temperature_c is not None and humidity is not None:
            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )

            if temperature_c > TEMPERATUR_SCHWELLE or humidity > FEUCHTIGKEIT_SCHWELLE:
                print("Achtung: Fenster sollten geöffnet werden, da die Temperatur oder Feuchtigkeit zu hoch ist.")

        time.sleep(60)

if __name__ == "__main__":
    main()
