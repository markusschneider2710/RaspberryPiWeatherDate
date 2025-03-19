# Raspberry Pi Weather + Date project

in this Raspberry Pi project I created a small Deskthing that projects the current time, the room temperature + humidity and also the weather from the outside. 

<img src="https://github.com/user-attachments/assets/3bb918e6-a601-4374-a3b2-8072e0ca0a2f" width="400" />

<details>
<summary>Used Hardware for this project</summary>

|Items | Use case |
|-----:|-----------|
|Raspberry Pi Zero 2 W +  ||
|DHT11  | inside temperarture and humidity    |
|DS3231  | a real time clock + date       |
|4.2" Waveshare e-paper display  | to display the information|
|Openweathermap API | to get outside weather information |

</details>

<p>
To get the Pi running I installed Raspberry Pi OS from the following site: [Raspberry OS](https://www.raspberrypi.com/software/) and made it headless.

After installing and setting everything up we go straight to connect the DHT11 sensor to the Raspberry itself.

To get the DHT11 running and have everything installed right, i used the following site to understand the working process: https://docs.sunfounder.com/projects/umsk/en/latest/05_raspberry_pi/pi_lesson19_dht11.html

After setting the sensor with every needed libary up, i went and wrote some code in the terminal of the Pi using nano to get the inside temperature and humidity. (You can see the code @ dht11_sensor.py)

Seeing that the sensor spits out data I went and wrote also code to gather outside temperatures using an API-Key from OpenWeatherMap (see code @ openweathermap.py)

The next step is to connect and setting up the DS3231 RTC to get the real time. I used follwing tutorial to set it up: https://maker.pro/raspberry-pi/tutorial/how-to-add-an-rtc-module-to-raspberry-pi.

Setting up the necessary things, i started to set up the e-paper dislpay using the guide from Waveshare: https://www.waveshare.com/wiki/4.2inch_e-Paper_Module_Manual#Working_With_Raspberry_Pi

After setting everything up I wrote code to display everything I need. (see code @ code.py)
</p>
