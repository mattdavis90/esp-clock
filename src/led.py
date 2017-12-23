from machine import Pin
from utime import sleep_ms


class LED():
    OFF     = 0
    RED     = 1
    GREEN   = 2
    BLUE    = 3
    YELLOW  = 4
    CYAN    = 5
    MAGENTA = 6
    WHITE   = 7

    def __init__(self):
        self._red = Pin(4, Pin.OUT)
        self._green = Pin(9, Pin.OUT)
        self._blue = Pin(10, Pin.OUT)

        self.off()

    def on(self, colour=WHITE):
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
        self.on(self.OFF)

    def blink(self, t=500, colour=WHITE):
        self.on(colour)
        sleep_ms(t)
        self.off()
