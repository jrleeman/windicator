The wind vane design is downloaded from: http://www.thingiverse.com/thing:952978
Created by user micromet and distributed under the Creative Commons -
Attribution - Share Alike license.

## Instructions (from Thingiverse)

All plastic parts were printed with ABS using a Lulzbot Taz with an 0.35 mm nozzle. Use 30 to 40 % fill in all parts except the tail fin. The tail should be filled at 15 or 20 % to save some weight, making it easier to balance the vane with the nose counter weight.

Bill of Materials other than the 3D printed parts:
(2) M3 x 8 mm bolts
(2) M3 x 20 mm bolt
(1) M3x 12 mm bolt
(1) M5 x 10 mm bolt
(1) Continuous Turn 10K Potentiometer (two choices)
Bourns 6639S-1-103 ($17.40 at Digi-key, part number 6639S-1-103-ND)
Vishay Spectrol 157B103MX ($24.80 at Digi-key, part number 157B103MX-ND
(1) resistor (820K to 1M, not critical as long as in this range)
(1) 10-inch-long rod or tube, 3/16 inch outside diameter
Examples from McMaster Carr
2153T33 Rigid Carbon Fiber Shapes, Round Tube, .188" OD, .118" ID, 48" Length ($13,13)
86985K66 High-Strength 2024 Aluminum, Rod, 3/16" Diameter, 3' Long ($4.79)
(10 ft) of 22 awg 3 or 4 conductor cable
(1) Machine bolt (for nose weight) ½ inch bolt, 1 inch long

Special Tools Needed
M3 and M5 tap
soldering iron and solder
wire strippers

Assembly
Print Parts and coat with a UV resistant spray, e.g., clear Krylon fusion. ( recommended for long-term deployments) http://www.amazon.com/Krylon-2444-Fusion-Plastic-Clear/dp/B001TNMWBM
Tap M3 and M5 holes used later in assembly (see pics)
Solder resistor across the wiper and positive terminal on the potentiometer (pot). Tthis is required to prevent spurious analog voltage readings when the wiper on the continuous-turn pot "jumps" across the small gap between the 10K and 1 ohm position).
Solder the lead wires to the pot and install in the main body (see pics)
Apply silicone or epoxy where cable exits body to prevent water from entering around the cable.
Insert the heavy large machine nut into the nose piece (see pic), it should press fit or can be screwed in with a wrench.
Glue the nose cone or tip to covering the head of the large machine screw (super glue or 5-min epoxy).
Assemble the nose-piece, tail, and center piece to the 10-inch shaft. Slide the center piece until the vane is balance (see pic)
Attach the vane to the potentiometer assembly.
Tighten all the M3 setscrews on the tail, centerpiece, and nose.

Deployment
The system is designed for mounting on 1 inch pipe (1.33 inch O.D.) and secured with the M5 set screw. The standard deploy height for meteorological research is 2, 3 or 10 meters.
To correctly install, point the vane south with one hand, then rotate the base of the vane on the mounting pipe until the output on your data acquisition system (e.g., Arduino) reads 180 degrees. Then secure the base with the M5 set screw. This is much easier to do with two people.
If the pot is excited with 5V, then 0-5V will correspond to 0-360 degrees. Note, to correct for magnetic declination in your area.
http://www.ngdc.noaa.gov/geomag-web/#declination

A good anemometer to deploy with the vane is the vortex 3-cup unit from Inspeed
http://www.inspeed.com/anemometers/vortex_wind_sensor.asp
Note, a simple debouncing circuit will be needed to use the Vortex on the Arduino.

Pairing the DIY vane with the Vortex anemometer gives one a research grade wind measurement sensor package for under $90.

These instruments are easily interfaced with the Arduino, allowing calculation of mean wind speeds, statistical wind vectors, maximum, gusts, etc. A description of the wind vector calculation is provided here http://www.intellovations.com/2011/01/16/wind-observation-calculations-in-fortran-and-python/

An example Arduino program with notes is given here
https://gist.github.com/jaymham/7792782
