"""
pyther class
"""
__author__ = 'coop'

import cmd
import os
import sys
import pyther.module_loader as module_loader


class Pyther(cmd.Cmd):
    '''Pyther shell class'''
    def __init__(self, known_modules, path):
        cmd.Cmd.__init__(self)
        self.known_modules = known_modules
        self.path = path

    def get_custom_names(self):
        # This method used to pull in base class attributes
        # at a time dir() didn't do it yet.
        return self.known_modules

    def complete_custom_cmds(self, text, *ignored):
        return [a for a in self.get_custom_names() if a.startswith(text)]

    def completenames(self, text, *ignored):
        ret = cmd.Cmd.completenames(self, text, *ignored)
        ret.extend(self.complete_custom_cmds(text, *ignored))
        return ret

    def complete_custom_args(self, text, *ignored):
        # get argparse, extract all keys
        # or autocomplete argparse
        pass

    def do_quit(self, *ignore):
        '''Exit the shell'''
        return True

    def do_EOF(self, *ignore):
        '''^C + d'''
        return self.do_quit(*ignore)


    def do_help(self, arg):
        pass

    def default(self, lines):
        '''run customize commands'''
        loader = module_loader.Loader(self.path)
        line = lines.split(' ', 1)
        cmd = line[0]
        if len(line) > 1:
            args = line[1]
        else:
            args = None

        command = loader.load(cmd, cmd.title())
        command.run(args)
