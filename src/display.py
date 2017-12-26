from machine import Pin, SPI
from max7219 import Matrix8x8


def inc_column(idx, column, by=1):
    """Increment the index and column by the given amount

    :param idx: The current LED matrix
    :param column: The current column
    :param by: How much to move

    :return: Tuple of (idx, column)
    """
    column += by
    while column > 7:
        idx += 8
        column -= 8
    return (idx, column)


class Display():
    """Wrap the display
    Stores an internal character map

    :param spi_port: SPI port to use
    :param cs_pin: CS pin to use
    """
    characters = {
        '1': bytearray([0, 124, 0]),
        '2': bytearray([116, 84, 92]),
        '3': bytearray([84, 84, 124]),
        '4': bytearray([28, 16, 124]),
        '5': bytearray([92, 84, 116]),
        '6': bytearray([124, 84, 116]),
        '7': bytearray([4, 4, 124]),
        '8': bytearray([124, 84, 124]),
        '9': bytearray([92, 84, 124]),
        '0': bytearray([124, 68, 124]),
        ':': bytearray([40]),

        'P': bytearray([60, 126, 122, 126, 102, 36]), # Pacman
        'D': bytearray([0, 24, 24]),                  # Dot
        ' ': bytearray([0, 0, 0]),                    # Dot-sized space

        'H': bytearray([119, 231, 192, 192, 231, 119]), # Happy face
        'S': bytearray([231, 119, 48, 48, 119, 231]),   # Sad Face

        'W': bytearray([201, 217, 25, 115, 227, 7, 62, 252]), # WiFi
    }

    def __init__(self, spi_port, cs_pin):
        spi = SPI(spi_port, baudrate=10000000, polarity=0, phase=0)
        self.disp = Matrix8x8(spi, Pin(cs_pin), 4)

    def clear(self):
        """Clear the display buffer
        N.B. Show need calling to actually update the display
        """
        for i in range(len(self.disp.buffer)):
            self.disp.buffer[i] = 0

    def text(self, string, start=0):
        """Write text to the display buffer
        N.B. Show need calling to actually update the display
        N.B. There is no bounds checking. Don't write past the end of the display!

        :param string: The string to write
        :param start: Start column
        """
        for row in range(8):
            idx = 0
            column = start

            for c in string:
                data = self.characters.get(c, None)

                if data:
                    for i in range(len(data)):
                        self.disp.buffer[idx + row] |= ((data[i] >> row) & 1) << (7 - column)
                        idx, column = inc_column(idx, column)

                idx, column = inc_column(idx, column)

    def show(self):
        """Show the siaply buffer on the display
        """
        self.disp.show()


display = Display(1, 12)
