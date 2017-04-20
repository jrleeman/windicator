# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.

from time import sleep

import bigeasydriver

stepper = bigeasydriver.BigEasyDriver()
stepper.enable_pin = 5
stepper.MS1_pin = 6
stepper.MS2_pin = 13
stepper.MS3_pin = 19
stepper.direction_pin = 26
stepper.step_pin = 16

stepper.begin()

print("Moving CCW")
stepper.move_nsteps(100)
time.sleep(2)
print("Moving CW")
stepper.set_direction('cw')
stepper.move_nsteps(100)
