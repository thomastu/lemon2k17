# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import str

import json

# FUTURE FEATURE :
# resources
# Each resource should have a range of attributes
# Lemons might have a range of tartness, sweetness, etc.
# This is pretty much just to fill in data for regressions
# and the preferences mechanic for customers.
# Different suppliers will provide resources with different
# distributions of various resource attributes.
# Open Question : Variant vs supplier?  (i.e. meyer lemons, vs. Local Farm)
# from . import resources

class BaseRecipe(object):
    """Recipes determine resource costs and quality."""

    required = []

    def __init__(self, name, price, **ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return json.dumps(self.ingredients)

    def __repr__(self):
        return "<{} Recipe : {}>".format(self.__class__.__name__, self.name)

    @property
    def ingredients(self):
        return dict(self._ingredients)

    @ingredients.setter
    def ingredients(self, val):
        val = dict(val)
        for r in self.required:
            assert r in val, "{} must contain {}".format(self.__class__.__name__, r)
        D = []
        for i, N in val.items():
            N = float(N)
            assert N > 0., "Recipes have positive quantity of {}".format(str(i).capitalize())
            D.append((i, N))
        self._ingredients = D

    def adjust(self, **ingredients):
        """Adjust recipe."""
        D = self.ingredients
        D.update(ingredients)
        self.ingredients = D

class Lemonade(BaseRecipe):

    required = ["lemons", "sugar", "water"]

class Cookies(BaseRecipe):

    required = ["sugar", "flour"]
