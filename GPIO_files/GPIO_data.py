import time
import smbus2
import bme280
import asyncio
import RPi.GPIO as GPIO
from enum import Enum  
import aiohttp
import math
import requests

SERVO_PIN_1 = 13 
SERVO_PIN_2 = 12 
LIGHT_PIN = 26

class signal_type(Enum):
    HIGH = GPIO.HIGH
    LOW = GPIO.LOW


def get_BME280_Sensor():
    # BME280 sensor address (default address)
    address = 0x77

    # Initialize I2C bus
    bus = smbus2.SMBus(1)

    # Load calibration parameters
    calibration_params = bme280.load_calibration_params(bus, address)

    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    # Uncomment the following line to start a continuous loop
    # while True:
    try:
        # Read sensor data
        data = bme280.sample(bus, address, calibration_params,8)

        # Extract temperature, pressure, and humidity
        temperature_celsius = data.temperature
        pressure = data.pressure
        humidity = data.humidity

        # Convert temperature to Fahrenheit
        temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

        # Print the readings
        return (math.floor(humidity), math.floor(temperature_fahrenheit))

        # Wait for a few seconds before the next reading
        # time.sleep(2)

    # Removed the KeyboardInterrupt except block as it's not applicable outside of a loop in this context
    except Exception as e:
        print('An unexpected error occurred:', str(e))
        # No break needed here since we're not in a loop
def rotate_motor(angle):
      # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN_1, GPIO.OUT)
    GPIO.setup(SERVO_PIN_2, GPIO.OUT)

    pwm1 = GPIO.PWM(SERVO_PIN_1, 50)  # Initialize PWM on SERVO_PIN_1 at 50Hz
    pwm2 = GPIO.PWM(SERVO_PIN_2, 50)  # Initialize PWM on SERVO_PIN_2 at 50Hz
    
    # PWM on pin #13  at 50Hz
    pwm1.start(0)
    pwm2.start(0)
  


    def SetAngle(pwm, pin, angle):
        duty = angle / 18 + 2
        GPIO.output(pin, True)
        pwm.ChangeDutyCycle(duty)

    # Set angle for both servos first without delay
    SetAngle(pwm1, SERVO_PIN_1, angle)  # Set SERVO_PIN_1 to angle
    SetAngle(pwm2, SERVO_PIN_2, 180 - angle)  # Set SERVO_PIN_2 to inverse angle for opposite direction

    # Now wait for the servos to reach the position
    time.sleep(1)  # Wait enough time for the servo to reach the set angle

    # Turn off PWM signal
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    GPIO.output(SERVO_PIN_1, False)
    GPIO.output(SERVO_PIN_2, False)

    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

def get_light_status(): 
     # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LIGHT_PIN, GPIO.IN)
    return GPIO.input(LIGHT_PIN)
    



def set_light_status(state):
     # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LIGHT_PIN, GPIO.OUT)
    GPIO.output(LIGHT_PIN, state)
    GPIO.cleanup()

def get_gpio_frontend():
        # The URL you want to send the GET request to
    url = 'http://localhost:1337/api/gpios/1'

    # Sending a GET request to the URL
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        # The request was successful; you can process the response further
        print("Success!")
        data = response.json()
        servo = data['data']['attributes']['servo']
        light = data['data']['attributes']['light']
        temp = data['data']['attributes']['temp']  # Assuming you meant 'temp' instead of 'tap'
        hold = data['data']['attributes']['hold']
        return(servo,light, temp, hold)
    else:
        # The request failed; handle the failure
        print("Failed to retrieve data. Status code:", response.status_code)

if __name__ == "__main__":
   
    #get light current state
    light_state = get_light_status()
    GPIO.cleanup()
    servo, light, temp, hold = get_gpio_frontend()

    #servo motor set up 
    rotate_motor(servo)
    print(light_state, light)
    # if light_state is not light: 
    #     print()
    set_light_status(light)

    light_state = get_light_status()
    GPIO.cleanup()
    print(light_state)
    # Call the function to get the sensor data
    hummidity, temp = get_BME280_Sensor()

    print('hummidity:',hummidity,  'temp:',temp)





