# -*- coding: utf-8 -*-

import Queue
from threading import Thread

from . import recipes
from . import customers

class Vendor(object):

    def __init__(self, name, Location, Workers=list(), Owner=None, upgrades=None):
        """
        name, str : name of stand/vendor
        Location, ```places.Location`` : a defined location
        """
        self.name = name
        # self.location = None # This is set in Location.register
        Location.register(self)
        self.worker = worker
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

    @property
    def value(self):
        """Vendor net worth."""
        return 10.

    def sell(self, Customer, item, quantity=1):
        """Sells an item in stock to a customer."""
        if item in self.stock:  # Check if item is in stock
            # Check that there's enough
            if self.stock[item] >= quantity:
                price = self.menu[item]*quantity
                # Check the customer can afford
                assert Customer.money >= price
                Customer.money -= price
                self.money += price
                return True
            # Else do nothing for now
        return False

    def buy(self, Vendor, **items):
        """Method for restocking materials and material quantities."""
        for i, k in items:
            sold = Vendor.sell(self, i, k)
            if sold:
                self.inventory[i] += k


class Stand(Vendor):
    pass
