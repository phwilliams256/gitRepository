#  Phil H Williams
## In conjunction with Bob Belford in the IoST lab and Information Science - CSTEM, UA Little Rock.
#
# This project was supported by the Arkansas INBRE program, with a grant from
# the National Institute of General Medical Sciences, (NIGMS), P20 GM103429
# from the National Institutes of Health.

import time
import board
import adafruit_ahtx0

from busio import I2C

#  on the RPi Pico  GP4=pin7 and   GP5=pin8
i2c = I2C(sda=board.GP4, scl=board.GP5)
# Create sensor object, communicating over the board's default I2C bus
sensor = adafruit_ahtx0.AHTx0(i2c)

threshold = 56

while True:
  print("\nTemperature: %0.1f C" % sensor.temperature)
  rh = sensor.relative_humidity
  print("Humidity: %0.1f %%" % rh)

  if rh > threshold:
    print(" greater than threshold")
  time.sleep(2)
  