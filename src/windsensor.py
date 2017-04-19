"""Read wind sensors

Contains tools to read the wind sensors.
"""

import mcp3008

class windVane(object):
    r"""Wind Vane

    Contains utility for reading a wind vane that is based on a potentiometer.
    The user should orient the wind vane taking magnetic declination into
    account as we assume that the "north" resistance specified is true north.
    """

    def __init__(self):

        # Hardware pin connections
        self.adc_differential_pinset = None
        self.clk_pin = None
        self.cs_pin = None
        self.miso_pin = None
        self.mosi_pin = None

        # Hardware state information
        self.north_resistance = None
        self.resistance_increases = 'cw'
        self.potentiometer_range = 10000.
        self.v_excitation = 3.3


    def begin(self):
        """
        Initialize the hardware.
        """
        self.adc = mcp3008.MCP3008(clk=self.clk_pin, cs=self.cs_pin,
                                   miso=self.miso_pin, mosi=self.mosi_pin)
        return True


    def get_potentiometer_resistance(self, vout):
        """
        Get the resistance of the potentiometer.
        """
        return vout/self.v_excitation * self.potentiometer_range


    def get_wind_direction(self, navg=1):
        """
        Get the wind direction in degrees.

        returns the result of navg readings.
        """
        adc_reading_bits = 0
        for i in range(navg):
            adc_reading_bits += self.adc.read_adc_difference(self.adc_differential_pinset)
        adc_reading_bits /= navg
        adc_reading_volts = 3.3 / 1023 * adc_reading_bits
        potentiometer_resistance =self.get_potentiometer_resistance(adc_reading_volts)
        degrees_per_ohm = 360. / 10000
        wind_direction = potentiometer_resistance - self.north_resistance * degrees_per_ohm
        return wind_direction
