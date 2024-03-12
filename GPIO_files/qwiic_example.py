import qwiic
import qwiic_bme280
import time
import sys
from qwiic_oled_base import QwiicOledBase

# Scan for devices and list them
print("Scanning for Qwiic devices...")
addresses = qwiic.scan()
print(f"Found devices at addresses: {addresses}")

# Initialize the sensor
bme280 = qwiic_bme280.QwiicBme280()

# Check if the Qwiic BME280 device is connected
if not bme280.is_connected():
    print("The Qwiic BME280 device is not connected. Please check your connection.")
    exit()

bme280.temperature_oversample = 16

if not bme280.begin():
    print("The Qwiic BME280 device couldn't be initialized. Please check your connection.")
    exit()

# Retrieve the temperature in Celsius
temperature_celsius = bme280.get_temperature_celsius()

# Convert temperature to Fahrenheit
temperature_fahrenheit = temperature_celsius * 9/5 + 32

print(f'Current temperature: {temperature_fahrenheit:.2f} °F')


oled = QwiicOledBase()
oled.begin()
    
    # Clear the display
oled.clear(oled.ALL)
    
    # Read temperature
temperature = temperature_fahrenheit 
    
    # Format the temperature string
temp_str = f"Temp: {temperature:.1f} C"
    
    # Set cursor position where the temperature will be displayed
oled.set_cursor(0, 0)
    
    # Print the temperature string on the OLED
oled.print(temp_str)
    
    # Update the display to show the new data
oled.display()