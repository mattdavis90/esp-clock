import ntptime
import network
import utime
from display import inc_column


class NTP():
    def __init__(self, display):
        self._display = display
        self._current_ticks = 0
        self._previous_ticks = 0
        self._previous_connected = False
        self._sta_if = network.WLAN(network.STA_IF)

    def ready(self, current_ticks, now):
        self._current_ticks = current_ticks
        return True

    def show(self, now):
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


class PacMan():
    def __init__(self, display):
        self._display = display
        self._last_run = None
        self._running = False
        self._frame = 0

    def ready(self, current_ticks, now):
        if self._running or (now[5] in (0, 30) and now[5] != self._last_run): # Run at 0 and 30 secs. But only display at 0
            self._last_run = now[5]
            return True
        return False

    def show(self, now):
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


class Seconds():
    def __init__(self, display):
        self._display = display
        self._previous_ticks = 0

    def ready(self, current_ticks, now):
        if utime.ticks_diff(current_ticks, self._previous_ticks) > 100:
            self._previous_ticks = current_ticks
            return True
        return False

    def show(self, now):
        idx = 0
        column = 1

        for i in range(30):
            if (2 * i) < now[5]:
                self._display.disp.buffer[idx] |= 1 << (7 - column) # Write directly to the display buffer
            idx, column = inc_column(idx, column)

        return False


class Time():
    def __init__(self, display):
        self._display = display
        self._previous_ticks = 0

    def ready(self, current_ticks, now):
        if utime.ticks_diff(current_ticks, self._previous_ticks) > 200:
            self._previous_ticks = current_ticks
            return True
        return False

    def show(self, now):
        self._display.text('{:02d}:{:02d}:{:02d}'.format(now[3], now[4], now[5]), 2)

        return True
