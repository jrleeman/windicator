import time

import windsensor

wvane = windsensor.windVane()
wvane.adc_differential_pinset = 0
wvane.clk_pin = 11
wvane.cs_pin = 22
wvane.miso_pin = 9
wvane.mosi_pin = 10
wvane.north_resistance = 0.

wvane.begin()

while True:
    print(wvane.get_wind_direction())
    sleep(1)
