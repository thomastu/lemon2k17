# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cmd import Cmd
from .engine import Lemon2KEngine

class LemonConsole(Cmd):

    intro = "Welcome to Lemon 2k17 version 0.0.0b"
    prompt = "lemon2k17>>> "

    def __init__(self, *args, **kwargs):
        super(LemonConsole, self).__init__()
        self.engine = Lemon2KEngine(*args, **kwargs)

    def do_status(self, arg):
        """Display input status menu"""
        result = self.engine.status(arg)
        print(result)


def main():
    startup = raw_input("What is your name: ")
    REPL_SERVER = LemonConsole(startup)
    REPL_SERVER.cmdloop()
