# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.

from time import sleep

import ../bed

stepper = bed.BigEasyDriver()
stepper.enable_pin =
stepper.MS1_pin =
stepper.MS2_pin =
stepper.MS3_pin =
stepper.direction_pin =
stepper.step_pin =

stepper.begin()

print("Moving CCW")
stepper.move_nsteps(100)
time.sleep(2)
print("Moving CW")
stepper.set_direction('cw')
stepper.move_nsteps(100)
