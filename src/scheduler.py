import utime

from display import display
from pages import NTP, StarWars, PacMan, Seconds, Time


def run():
    """Run the page scheduler
    """
    pages = [NTP(display),
             StarWars(),
             PacMan(display),
             Seconds(display),
             Time(display)]

    clear_next = True

    while True:
        current_ticks = utime.ticks_ms()
        now = utime.localtime()

        for page in pages:
            if page.ready(current_ticks, now):
                if clear_next:
                    display.clear()

                clear_next = page.show(now)

                if clear_next:
                    display.show()
                    break

        utime.sleep_ms(5)
