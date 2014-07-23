"""
Default Plugin class for pyter

Inherit from this class if you write your own modules

Written by DerCoop <dercoop@users.sourceforge.net>

"""

__author__ = 'coop'
__license__ = 'GPLv2'

class Plugin:
    def __init__(self):
        print 'PytherPlugin: constructor'

    def run(self, args):
        print 'PytherPlugin: run'