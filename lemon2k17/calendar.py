# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep

class Calendar(object):
    """Keeps track of time starting with a starting date."""

    def __init__(self, day = 0., hour_length=60):
        self.day = day   # starting day
        self.paused = False
        self._hr = hour_length # Length of in-game hour in seconds
        self.hr = self.0
        self.run()

    @property
    def date(self):
        day = self.day // 1
        hr = (self.day*24) % 1
        return (day, hr)

    def increment_day(self):
        while not self.paused:
            sleep(1)
            self.hr += 1
            if self.hr >= self._hr:
                self.day += 1/24.  # Every minute is 1 hour
                self.hr = self._hr

    def run(self):
        time = Thread(target=self.increment_day)
        time.daemon = True
        time.start()

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False
