Adding New Pages
================

Open the `pages.py` file and add a new page class to the document. The new page should be
a class that extends the :py:class:`pages.Page` class.

Implement a `ready` and `show` method.

.. code-block:: python

    class Time(Page):
        def __init__(self, display):
            self._display = display
            self._previous_ticks = 0

        def ready(self, current_ticks, now):
            # Run if 200 ticks have passed
            if utime.ticks_diff(current_ticks, self._previous_ticks) > 200:
                self._previous_ticks = current_ticks
                return True
            return False

        def show(self, now):
            # Show the time
            self._display.text('{:02d}:{:02d}:{:02d}'.format(now[3], now[4], now[5]), 2)
            return True

Add the new page to the scheduler in :py:meth:`scheduler.run`.

.. code-block:: python

    def run():
        """Run the page scheduler
        """
        pages = [NTP(display),
                 StarWars(),
                 PacMan(display),
                 Seconds(display),
                 Time(display)]      # <----- Add it here

Now upload the updated files using `ampy` from `Adafruit <https://github.com/adafruit/ampy>`_, which can be installed with `pip`.

.. code-block:: bash

    pip install adafruit-ampy
    ampy -p /dev/ttyUSB0 put pages.py
    ampy -p /dev/ttyUSB0 put scheduler.py
