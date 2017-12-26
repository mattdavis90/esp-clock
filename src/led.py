from machine import Pin
from utime import sleep_ms


class LED():
    """Wrap an RGB LED

    Defines a number of colours to display

    :param red_pin: The pin the Red LED is attached to
    :param green_pin: The pin the Green LED is attached to
    :param blue_pin: The pin the Blue LED is attached to
    """
    OFF     = 0
    RED     = 1
    GREEN   = 2
    BLUE    = 3
    YELLOW  = 4
    CYAN    = 5
    MAGENTA = 6
    WHITE   = 7

    def __init__(self, red_pin, green_pin, blue_pin):
        self._red = Pin(red_pin, Pin.OUT)
        self._green = Pin(green_pin, Pin.OUT)
        self._blue = Pin(blue_pin, Pin.OUT)

        self.off()

    def on(self, colour=WHITE):
        """Turn the LED on with the specified colour

        :param colour: The colour to show. Must be an int.
        """
        if colour in (self.OFF, self.GREEN, self.BLUE, self.CYAN):
            self._red.on()
        else:
            self._red.off()

        if colour in (self.OFF, self.RED, self.BLUE, self.MAGENTA):
            self._green.on()
        else:
            self._green.off()

        if colour in (self.OFF, self.RED, self.GREEN, self.YELLOW):
            self._blue.on()
        else:
            self._blue.off()

    def off(self):
        """Turn the LED off
        """
        self.on(self.OFF)

    def blink(self, t=500, colour=WHITE):
        """Blink the LED on with the specified colour for a given time

        :param t: Time to blink (ms)
        :param colour: The colour to show. Must be an int.
        """
        self.on(colour)
        sleep_ms(t)
        self.off()


led = LED(4, 9, 10)
