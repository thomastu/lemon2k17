# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from time import sleep
from random import randint

class Customer(object):

    def __init__(self, name="Bob", money=5.):
        self.name = name
        self.money = money

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)

    def lineup(self):
        """Decides whether customer lines up.
        """
        return bool(randint(0, 1))

def generate_customers(vendor):
    """Generates customers for a vendor."""
    while vendor.is_open:
        # In future, this should come from a global pool.  There should be limited customers.
        # Each customer should also decide whether or not to go to your lemonade stand or a rival one.
        c = Customer()
        if c.lineup():
            vendor.customers.put(c)
        # Uniform binary distribution is very boring
        # Try Poisson or create some weather dependent distribution.
        sleep(5)
