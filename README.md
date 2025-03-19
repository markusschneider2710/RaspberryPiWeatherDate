# Raspberry Pi Weather + Date project

In this Raspberry Pi project, I designed a small desk display that shows the current time, room temperature and humidity and outside weather updates

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

# Project Overview
To get started with this project, I installed Raspberry Pi OS from the official Raspberry Pi website: [Raspberry OS](https://www.raspberrypi.com/software/). I configured the Raspberry Pi to run headlessly.

## Setup Steps

### 1. DHT11 Sensor Setup
- I connected the DHT11 sensor to the Raspberry Pi and followed the setup instructions from [SunFounder's documentation](https://docs.sunfounder.com/projects/umsk/en/latest/05_raspberry_pi/pi_lesson19_dht11.html) to ensure all necessary libraries were installed.
- Using the terminal, I wrote a Python script (`dht11_sensor.py`) to read the indoor temperature and humidity.

### 2. OpenWeatherMap API Integration
- I used an API key from OpenWeatherMap to fetch outside temperatures. The code for this is available in `openweathermap.py`.

### 3. DS3231 RTC Setup
- To obtain real-time data, I set up the DS3231 RTC module using the tutorial from [Maker Pro](https://maker.pro/raspberry-pi/tutorial/how-to-add-an-rtc-module-to-raspberry-pi).

### 4. E-Paper Display Setup
- I configured the e-paper display using the guide provided by [Waveshare](https://www.waveshare.com/wiki/4.2inch_e-Paper_Module_Manual#Working_With_Raspberry_Pi).

### 5. Final Code
- After setting up all components, I wrote a comprehensive script (`code.py`) to display the necessary data on the e-paper display.

## Example Use Cases
- **Indoor Temperature and Humidity Monitoring**
- **Outdoor Weather Updates**
- **Real-Time Display on E-Paper**
