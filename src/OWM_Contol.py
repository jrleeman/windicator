import json
import os
from urllib.request import urlopen
from urllib.parse import quote
import time
import bigeasydriver
import RPi.GPIO as GPIO
import numpy as np


def get_weather(query):
    try:
        api_url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&appid={1}'
        query = quote(query)
        url = api_url.format(query, os.environ.get('OPENWXMAP_API_KEY', None))
        data = urlopen(url).read()#.decode('utf-8')
        parsed = json.loads(data)
        weather = None
        if parsed.get('weather'):
            weather = {'temperature':parsed['main']['temp'],
                       'humidity':parsed['main']['humidity'],
                       #'pressure':parsed['main']['sea_level'],
                       'windspeed':parsed['wind']['speed'],
                       'winddeg':parsed['wind']['deg']}
    except:
        print("ERROR")
        weather = {'temperature':-999,
                   'humidity':-999,
                   #'pressure':parsed['main']['sea_level'],
                   'windspeed':-999,
                   'winddeg':0}
    return weather

def calculate_move(current_direction, new_direction):
    delta_degrees = new_direction - current_direction
    if current_direction + delta_degrees > 360:
        delta_degrees -= 360
        delta_degrees = delta_degrees * -1
    return delta_degrees, current_direction + delta_degrees


def move_camera(current_direction, move):
    """
    Positive = CCW
    """
    if move >0 :
        stepper.enable()
        stepper.set_direction('ccw')
        actual_move = stepper.move_degrees(move)
        stepper.disable()

    elif move < 0:
        stepper.enable()
        stepper.set_direction('cw')
        actual_move = stepper.move_degrees(np.abs(move))
        stepper.disable()

    else:
        stepper.disable()
        move = 0

    return current_direction + move


def take_photo():
    pass

if __name__ == '__main__':

    # Setup the big easy driver
    stepper = bigeasydriver.BigEasyDriver()
    stepper.enable_pin = 5
    stepper.MS1_pin = 6
    stepper.MS2_pin = 13
    stepper.MS3_pin = 19
    stepper.direction_pin = 26
    stepper.step_pin = 16

    stepper.begin()
    stepper.degrees_per_step = 1.8
    stepper.set_stepsize('full step')
    stepper.disable()

    # Start with everything pointing at 180
    current_direction = 180.
    while True:
        # Get weather
        weather = get_weather('Mead,CO')

        # Calculate move
        delta_degrees, current_direction = calculate_move(current_direction, weather['winddeg'])
        print("Moving {0} to point to {1} ".format(delta_degrees, current_direction))

        # Point into wind
        move_camera(current_direction, delta_degrees)

        # Take photo


        # Wait for next minute
        time.sleep(60)
