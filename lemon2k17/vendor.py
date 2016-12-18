# -*- coding: utf-8 -*-

import Queue
from threading import Thread

from . import recipes
from . import customers

class Vendor(object):

    def __init__(self, name):
        self.name = name
        self.money = 0.
        self.customers = Queue.Queue()
        self.is_open = False
        self.inventory = {"lemons" : 5., "sugar" : 5., "ice" : 3.}

    def open(self):
        """Opens up lemonade stand allowing customers to queue up."""
        self.is_open = True
        t = Thread(target = customers.generate_customers, args=[self])
        t.daemon = True
        t.start()

    def close(self):
        """CLoses up shop for the day, clears customer queue."""
        while not self.customers.empty():
            customer = self.customers.get()
            # Customer should react if kicked out without getting lemonade. e.g.:
            # print "{} left angrily".format(customer)
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
