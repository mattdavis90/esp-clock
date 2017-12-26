from micropython import const


_NOOP = const(0)
_DIGIT0 = const(1)
_DECODEMODE = const(9)
_INTENSITY = const(10)
_SCANLIMIT = const(11)
_SHUTDOWN = const(12)
_DISPLAYTEST = const(15)


class Matrix8x8:
    """Wrap the MAX7219 Matrix driver

    :param spi: The SPI port to use
    :param cs: The CS pin to use
    :param num: The number of matrices
    """
    def __init__(self, spi, cs, num):
        self._spi = spi
        self._cs = cs
        self._cs.init(cs.OUT, True)
        self._num = num

        self.buffer = bytearray(8 * num)
        self.init()

    def _write(self, command, data):
        """Write the command to the driver

        :param command: The command to write
        :param data: The data to write
        """
        self._cs(0)
        for m in range(self._num):
            self._spi.write(bytearray([command, data]))
        self._cs(1)

    def init(self):
        """Initialise the display driver
        """
        for command, data in (
            (_SHUTDOWN, 0),
            (_DISPLAYTEST, 0),
            (_SCANLIMIT, 7),
            (_DECODEMODE, 0),
            (_SHUTDOWN, 1),
        ):
            self._write(command, data)

    def brightness(self, value):
        """Set the display brightness

        :param value: The birghtness. Between 0 and 15 inc.
        """
        if not 0 <= value <= 15:
            raise ValueError("Brightness out of range")
        self._write(_INTENSITY, value)

    def show(self):
        """Show the display buffer
        """
        for y in range(8):
            self._cs(0)
            for m in range(self._num):
                self._spi.write(bytearray([_DIGIT0 + y, self.buffer[(m * 8) + y]]))
            self._cs(1)
