# Raspberry Pi Weather + Date project
Raspberry Pi weather and date project 

in tihs Raspberry Pi project I want to create a small Deskthing that projects the current time, the room temperature + humidity and also the weather from the outside. 

<h1>Used Hardware:</h1>

Raspberri Pi Zero 2 W +

DHT11 -> inside temperarture and humidity

DS3231 -> a real time clock + date

2.7" Waveshare e-paper display -> to display the information

Openweathermap API -> to get outside weather information

To get the Pi running i installed Raspberry Pi OS from the following site: https://www.raspberrypi.com/software/

After installing an setting everything up we go straight to connect the DHT11 sensor to a breadboard and to the Raspberry itself.

To get the DHT11 running and have everything installed right, i used the following site: https://docs.sunfounder.com/projects/umsk/en/latest/05_raspberry_pi/pi_lesson19_dht11.html

After setting the sensor with every needed libary up, i went and wrote some code in the terminal of the Pi using nano to get the inside temperature and humidity. (You can see the code @ dht11_sensor.py)

Seeing that the sensor spits out data I went and wrote also code to gather outside temperatures using an API-Key from OpenWeatherMap (see code @ openweathermap.py)

As i am lazy and do not want to start both codes seperatly, I wrote a script to open up both codes at the same time. (see code @ parallel.py)
