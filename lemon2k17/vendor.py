# -*- coding: utf-8 -*-

import queue
from threading import Thread

from . import recipes

class Vendor(object):

    def __init__(self, name):
        self.name = name
        self.bank = 0.
        self.customers = queue.Queue()
        self.is_open = False
        self.inventory = {"lemons" : 5., "sugar" : 5., "ice" : 3.}

    def open(self):
        """Opens up lemonade stand allowing customers to queue up."""
        self.is_open = True
        t = Thread(target = customers.generate_customers, args=[self.customers, self])
        t.daemon = True
        t.start()

    def close(self):
        """CLoses up shop for the day, clears customer queue."""
        while self.customers.not_empty():
            customer = self.customers.get()
            # Customer should react if kicked out without getting lemonade.
        self.is_open = False

class Inventory(object):
    pass

class Supplier(object):
    """Suppliers provide raw materials to create products."""

    def __init__(self, quality = 5, price_level=5):
        self.quality = quality

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, val):
        assert 0 < val < 11, "Quality must be between 1 and 10"
        self._quality = val
