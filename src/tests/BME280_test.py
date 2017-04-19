from time import sleep

import bme280

while True:
    print(bme280.readBME280All())
    sleep(1)
