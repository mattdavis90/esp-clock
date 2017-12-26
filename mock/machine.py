class Pin():
    IN = 0
    OUT = 1

    def __init__(self, pin, direction=IN):
        pass

    def init(self, direction, value=0):
        pass

    def __call__(self, value):
        pass

    def off(self):
        pass

    def on(self):
        pass

    def value(self):
        return 0


class SPI():
    def __init__(self, spi_port, baudrate, polarity, phase):
        pass

    def write(self, data):
        pass


class PWM():
    def __init__(self, pin):
        pass

    def duty(self, duty):
        pass

    def deinit(self):
        pass

    def freq(self, f):
        pass

    def init(self):
        pass
