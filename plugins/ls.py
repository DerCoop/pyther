"""
    implementation of a system command

    example implementation of the unix 'ls' command with all options

    Written by DerCoop <dercoop@users.sourceforge.net>

"""

__author__ = 'coop'
__license__ = 'GPLv2'


import subprocess
import shlex
from plugin import Plugin


class Ls(Plugin):
    def __init__(self):
        # do not print the default stuff from the main pyther plugin
        pass

    @staticmethod
    def run(args):
        cmd = ['ls']
        if args:
            cmd.extend(shlex.split(args))
        print subprocess.check_output(cmd)
        return
