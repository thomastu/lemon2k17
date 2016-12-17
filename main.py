from time import sleep
from threading import Thread
from Queue import Queue

from random import randint

STORE = {
    "lemons" : .5,
    "sugar" : .1,
    "cups" : .25
}


class Vendor(object):

    def __init__(self, name, queue):
        self.name = name
        self.stock = {
            "lemons" : 0,
            "sugar" : 5,
            "cups" : 5,
        }
        self.money = 10.
        self.queue= queue

    def view_queue(self):
        print self.queue.queue

    def view_stock(self):
        for k, v in self.stock.items():
            print("{} : {}".format(k.upper(), v))

    def buy_stock(self):
        prices = "\n".join(["{} cost {}".format(k, v) for k, v in STORE.items()])
        x = raw_input("What would you like to buy? \n{}\n".format(prices))
        n = raw_input("How many {} would you like to buy ? ".format(x))
        self.stock[x] += int(n)

    def status(self):
        print "CURRENT STOCK : "
        self.view_stock()
        print "CURRENT CUSTOMER QUEUE :"
        self.view_queue()

class Customer(object):

    def __str__(self):
        return "Customer"

    def __repr__(self):
        return str(self)

    def lineup(self):
        return bool(randint(0, 1))


def start():
    name = raw_input("Input Name : ")
    customer_queue = Queue()
    customer_thread = Thread(target = generate_customers, args=[customer_queue])
    customer_thread.daemon = True
    customer_thread.start()
    return Vendor(name,customer_queue)

def generate_customers(queue):
    while True:
        sleep(5)
        c = Customer()
        if c.lineup():
            queue.put(c)

def dispatch(vendor, cmd):
    f = getattr(vendor, cmd, None)
    if callable(f):
        f()
    else:
        print f

def run(vendor):
    cmd = raw_input("What would you like to do ? ")
    dispatch(vendor, cmd)

if __name__ == "__main__":
    v = start()
    while True:
        try:
            run(v)
        except Exception as e:
            print("Encountered unexpected error : {}".format(e))
