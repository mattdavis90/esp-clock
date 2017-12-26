from machine import Pin, PWM
from utime import sleep_ms


melody = (
    (262, 125),
    163,
    (196, 63),
    82,
    (196, 63),
    82,
    (220, 125),
    163,
    (196, 125),
    450,
    (247, 125),
    163,
    (262, 125),
)


class Buzzer():
    """Wrap a buzzer

    :param pin: The pin the buzzer is attached to
    """
    def __init__(self, pin):
        self._pin = Pin(pin)
        self._pwm = PWM(self._pin)
        self.off()

    def on(self, f=440):
        """Turn the buzzer on

        :param f: The frequency to buzz at
        """
        self._pwm.freq(f)
        self._pwm.duty(512)
        self._pwm.init()

    def off(self):
        """Turn the buzzer off
        """
        self._pwm.duty(0)
        self._pwm.deinit()
        self._pin.off()

    def buzz(self, f=440, t=500):
        """Buzz at a given frequency for a given time

        :param f: The frequency to buzz at
        :param t: The time to buzz (ms)
        """
        self.on(f)
        sleep_ms(t)
        self.off()

    def tune(self, sequence=melody):
        """Play a tune

        :param sequence: Sequence of tuple (freq, time)
        """
        idx = 0
        while idx < len(sequence):
            f, t = sequence[idx]
            idx += 1
            self.buzz(f, t)
            if idx < len(sequence):
                t = sequence[idx]
                idx += 1
                sleep_ms(t)


buzzer = Buzzer(5)
