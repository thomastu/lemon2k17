# -*- coding: utf-8 -*-

from __future__ import unicode_literals

class Location(object):
    """
    Represents a location inside lemon2k17.

    Events, population characteristics can be set here.
    """

    neighbors = list()
    max_vendors = 10.  # for now, but should be function of demand curve

    class Population:
        """Represents a population in some location."""

        __N = 500  # population amount, fixed for now.  Make callable?
        # for future
        # ----------
        # for attr in dir(Population):
        #      build_dist(attr)

    def __init__(self, name):
        self.name = name
        self._vendors = dict()

    def register(self, vendor, date):
        """
        Register a vendor to a location.  More competition should affect demand curve.
        """
        if vendor.location is not self:
            loc.unregister(vendor.location)
        vendor.location = self
        self._vendors[vendor] = {"date_registered" : date}

    def unregister(self, vendor):
        return self._vendors.pop(vendor, None)

    @property
    def vendors(self):
        """Returns list of open vendors."""
        return [v for v in self._vendors if v.is_open()]
