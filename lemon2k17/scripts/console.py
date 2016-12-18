# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cmd import Cmd
from ..engine import Lemon2KEngine

class LemonConsole(Cmd, object):
    """Command-line interface for the lemon2k17 game.

    Using the latest technology (and the builtin cmd module), we provide a
    highly advanced API to manage your lemonade empire from the bash shell.
    """
    intro = "Welcome to Lemon 2k17 version 0.0.0b"
    prompt = "lemon2k17 >>> "

    def __init__(self, *args, **kwargs):
        super(LemonConsole, self).__init__()
        self.engine = Lemon2KEngine(*args, **kwargs)

    def do_status(self, arg):
        """Display input status menu"""
        result = self.engine.status(arg)
        if callable(result):
            print(result(arg))
        else:
            print(result)

    def do_open(self, arg):
        self.engine.vendor.open()

    def do_close(self, arg):
        self.engine.vendor.close()

    # Management commands
    def do_exit(self, *args):
        # Exit should save, but that means we need a save method
        # self.engine.save()
        return True


def main():
    startup = raw_input("What is your name: ")
    REPL_SERVER = LemonConsole(startup)
    REPL_SERVER.cmdloop()
