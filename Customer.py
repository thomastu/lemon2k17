from time import sleep
from threading import Thread
from Queue import Queue

from random import randint


def generate_customers(queue):
    while True:
        sleep(5)
        c = Customer()
        if c.lineup():
            queue.put(c)

class Customer(object):

    def __str__(self):
        return "Customer"

    def __repr__(self):
        return str(self)

    def lineup(self):
        return bool(randint(0, 1))


