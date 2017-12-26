import ntptime
import network
import utime

from display import inc_column
from led import led
from starwars import starwars
from button import button


class Page():
    """Define a page
    """
    def ready(self, current_ticks, now):
        """Is this page ready to run?

        :param current_ticks: The current system ticks
        :param now: The current time

        :return: Ready to run?
        """
        pass

    def show(self, now):
        """Display this page

        :param now: The current time

        :return: Finished showing for this schedule
        """
        pass


class NTP(Page):
    """Page to check the clock is connected to WiFi and get time from NTP
    """
    def __init__(self, display):
        self._display = display
        self._current_ticks = 0
        self._previous_ticks = 0
        self._previous_connected = False
        self._sta_if = network.WLAN(network.STA_IF)

    def ready(self, current_ticks, now):
        """Is this page ready to run?

        :param current_ticks: The current system ticks
        :param now: The current time

        :return: Ready to run?
        """
        self._current_ticks = current_ticks
        return True

    def show(self, now):
        """Display this page

        :param now: The current time

        :return: Finished showing for this schedule
        """
        if not self._sta_if.isconnected():
            self._display.text('WS', 0)

            return True
        elif not self._previous_connected or utime.ticks_diff(self._current_ticks, self._previous_ticks) > 300000: # every 5 mins
            self._previous_ticks = self._current_ticks
            try:
                ntptime.settime()

                if not self._previous_connected:
                    self._display.text('WH', 0)
                    self._previous_connected = True
                    return True
            except OSError:
                return True

        return False


class StarWars(Page):
    """Page to play StarWars on button press
    """
    def __init__(self):
        pass

    def ready(self, current_ticks, now):
        """Is this page ready to run?

        :param current_ticks: The current system ticks
        :param now: The current time

        :return: Ready to run?
        """
        return button.down

    def show(self, now):
        """Display this page

        :param now: The current time

        :return: Finished showing for this schedule
        """
        led.on(led.RED)
        starwars.play()
        led.off()
        return False


class PacMan(Page):
    """Page to show PacMan moving across the screen
    """
    def __init__(self, display):
        self._display = display
        self._last_run = None
        self._running = False
        self._frame = 0

    def ready(self, current_ticks, now):
        """Is this page ready to run?

        :param current_ticks: The current system ticks
        :param now: The current time

        :return: Ready to run?
        """
        if self._running or (now[5] in (0, 30) and now[5] != self._last_run): # Run at 0 and 30 secs. But only display at 0
            self._last_run = now[5]
            return True
        return False

    def show(self, now):
        """Display this page

        :param now: The current time

        :return: Finished showing for this schedule
        """
        if now[5] != 0: # Only run on the 30s mark
            return False

        if not self._running:
            self._running = True

        pacman = '{}P{}'.format(' '*self._frame, 'D'*(6 - self._frame))

        self._display.text(pacman, 1)

        if self._frame >= 6:
            self._running = False
            self._frame = 0
        else:
            self._frame += 1

        return True


class Seconds(Page):
    """Page to show a seconds ticker across the top of the screen
    """
    def __init__(self, display):
        self._display = display
        self._previous_ticks = 0

    def ready(self, current_ticks, now):
        """Is this page ready to run?

        :param current_ticks: The current system ticks
        :param now: The current time

        :return: Ready to run?
        """
        if utime.ticks_diff(current_ticks, self._previous_ticks) > 100:
            self._previous_ticks = current_ticks
            return True
        return False

    def show(self, now):
        """Display this page

        :param now: The current time

        :return: Finished showing for this schedule
        """
        idx = 0
        column = 1

        for i in range(30):
            if (2 * i) < now[5]:
                self._display.disp.buffer[idx] |= 1 << (7 - column) # Write directly to the display buffer
            idx, column = inc_column(idx, column)

        return False


class Time(Page):
    """Page to show the current time
    """
    def __init__(self, display):
        self._display = display
        self._previous_ticks = 0

    def ready(self, current_ticks, now):
        """Is this page ready to run?

        :param current_ticks: The current system ticks
        :param now: The current time

        :return: Ready to run?
        """
        if utime.ticks_diff(current_ticks, self._previous_ticks) > 200:
            self._previous_ticks = current_ticks
            return True
        return False

    def show(self, now):
        """Display this page

        :param now: The current time

        :return: Finished showing for this schedule
        """
        self._display.text('{:02d}:{:02d}:{:02d}'.format(now[3], now[4], now[5]), 2)

        return True
