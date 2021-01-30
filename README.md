# Generative Art
COMS 3930 Homework 1

Through this assignment I chose the topic of weather.
The purpose of the assignment is to familiarize with Raspberry Pi and Processing.

# Materials
- Raspberry Pi 4
- 8 RGB LED Module
- Female to Female Wires
- 5V Power Source
- External Keyboard/Mouse/Monitor

# Hardware
8 RGB LED Module required 3 INPUTS: Source, 5 Volts and Ground. With the female-to-female wires they were connect to the Raspberry Pi 4 pins GPIO 18, 5V Power and Ground respectively.

# Software
Neopixel/API Portion - The project was adapted from https://learn.adafruit.com/neopixels-on-raspberry-pi. I used OpenWeatherMap API which can find the current temperature based on lan and long coordinates. The program results in showing the corresponding color based on temperature and it lights up a certain amount of leds based on the tenths digit of the current temperature.

Processing Portion - I started off with a processing example called ball collision. There are 4 ball objects that appear in random sizes and go at different velocities. The colors are related to the different temperature that weathers can represent from red to blue or hot to cold. If balls collide it changes based on which red value is the greatest between them.

In order to run program on boot:
- Clone directory to Desktop: cd /home/pi/Desktop; git clone https://github.com/jxm033f/weather-api-art.git
- Open rc.local: sudo nano /etc/rc.local
- Add line before exit 0: sudo python3 /home/pi/Desktop/weather-api-art/weatherAPI.py &
- Open autostart: sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
- Add line at the very end: /usr/local/bin/processing-java --sketch=/home/pi/Desktop/weather-api-art/weatherCollision --run &

Youtube Link: https://youtu.be/f01RQblXVcM
