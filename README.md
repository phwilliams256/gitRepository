Overview:
This python script runs on the Raspberry Pi Pico W using the CircuitPython bootloader. The adafruit_ahtx0 library must be installed in the lib folder on the RPi Pico for this to work. 

The script work for both the AHT20 and the AHT10 Temperature & Humidity Sensors
These sensors communicate through I2c.
 
Wiring:
Physical pins 6 and 7 are GP4 and GP5 respectively. These are the default I2c connections. GP4 is SDA and GP5 is SCL. You can modify the script and the change GP pins to match your use case.

