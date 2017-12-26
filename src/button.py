from machine import Pin


class Button():
    """Wrap a button to make it easier to use

    :param pin: The pin the button is attached to
    :param invert: Is the pin inverted
    """
    def __init__(self, pin, invert=False):
        self._pin = Pin(pin)
        self._pin.init(Pin.IN)
        self._invert = invert

    @property
    def down(self):
        """Is the pin down
        :return: Pin is down
        """
        return self._pin.value() == 0 if self._invert else self._pin == 1

    @property
    def up(self):
        """Is the pin up
        :return: Pin is up
        """
        return self._pin.value() == 1 if self._invert else self._pin == 0


button = Button(2, True)
