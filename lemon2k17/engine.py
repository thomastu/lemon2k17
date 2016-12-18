# -*- coding: utf-8 -*-
"""
Using the latest technology, the Lemon2K17 engine manages the lemon2k17 universe.

This will eventually become a monolithic mega-class that powers a single game session.
"""
from .vendor import Vendor

class Lemon2KEngine(object):
    """Loads initial lemon2k17 universe."""

    def __init__(self, name):
        self.vendor = Vendor(name)

    def status(self, menu=None):
        if menu == "customers":
            return list(self.vendor.customers.queue)
        if hasattr(self.vendor, menu):
            return getattr(self.vendor, menu)
        else:
            return "Invalid menu."
