# -*- coding: utf-8 -*-

from queue import Queue

from .vendor import Vendor

class Lemon2KEngine(object):
    """Loads initial lemon2k17 universe."""

    def __init__(self, name):
        self.vendor = Vendor(name)

    def status(self, menu=None):
        if menu == "money":
            return self.vendor.money
        else:
            return "Invalid Status"
