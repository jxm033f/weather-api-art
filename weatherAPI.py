import board
import json
import neopixel
import requests
import time

time.sleep(30)

#api and location information
api_key = "490a5a33da6ecfbad4c3dc91138d9a12"
lat = 40.712776
lon = -74.005974
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, api_key)

#api connection and receiving data
response = requests.get(url)
data = json.loads(response.text)

#parse for current temp and store tenths digit
current_temp = data["current"]["temp"]
tensdigit = int(current_temp//10)

#directory of color corresponding to temp
color_dict = {1: (90,79,207),
              2: (0,72,186),
              3: (0,169,199),
              4: (38,230,0),
              5: (255,244,79),
              6: (255,130,67),
              7: (252,108,133),
              8: (201,0,22)}

#clear pixels
pixels = neopixel.NeoPixel(board.D18, 8, brightness=0.1, auto_write=False)
pixels.fill((0,0,0))
pixels.show()

#changes pixel color based on tenths digit (exception: >8 == 8 and <1 == 1)
if tensdigit < 1:
    pixels = neopixel.NeoPixel(board.D18, 1, brightness=0.1, auto_write=False)
    while True:
        pixels.fill(color_dict[1])
        pixels.show()
elif tensdigit > 8:
    pixels = neopixel.NeoPixel(board.D18, 8, brightness=0.1, auto_write=False)
    while True:
        pixels.fill(color_dict[8])
        pixels.show()
else:
    pixels = neopixel.NeoPixel(board.D18, tensdigit, brightness=0.1, auto_write=False)
    while True:
        pixels.fill(color_dict[tensdigit])
        pixels.show()