# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.

"""Windicator control program

The main control for the windicator project.
"""
import configparser

import bigeasydriver as bed
import bme280
import windsensor

# Startup
def startup():
    # Read the config fig
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')

    # Stepper driver and motor setup
    stepper = bed.BigEasyDriver()
    stepper.enable_pin = int(Config.get('motor', 'enable_pin'))
    stepper.MS1_pin = int(Config.get('motor', 'MS1_pin'))
    stepper.MS2_pin = int(Config.get('motor', 'MS2_pin'))
    stepper.MS3_pin = int(Config.get('motor', 'MS3_pin'))
    stepper.step_pin = int(Config.get('motor', 'step_pin'))
    stepper.direction_pin = int(Config.get('motor', 'direction_pin'))
    stepper.begin()
    
    # No BME280 Startup Required Currently

    # Wind vane setup
    wvane = windsensors.windVane()
    wvane.adc_differential_pinset = int(Config.get('MCP3008', 'adc_differential_pinset'))
    wvane.clk_pin = int(Config.get('MCP3008', 'adc_clk_pin'))
    wvane.cs_pin = int(Config.get('MCP3008', 'adc_cs_pin'))
    wvane.miso_pin = int(Config.get('MCP3008', 'adc_miso_pin'))
    wvane.mosi_pin = int(Config.get('MCP3008', 'adc_mosi_pin'))
    wvane.north_resistance = float(Config.get('windvane', 'north_resistance'))

    # Setup camera

# Establish orientation

# Read Windspeed

#

# Rotate camera

# Capture photo

# Shutdown
