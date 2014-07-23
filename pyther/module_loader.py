"""
Dynamic module loader for pyter

Written by DerCoop <dercoop@users.sourceforge.net>

"""
__author__ = 'coop'
__license__ = 'GPLv2'


import sys


class Loader:
    def __init__(self, path):
        sys.path.insert(0, path)

    @staticmethod
    def load(module_name, class_name):
        try:
            if module_name in sys.modules:
                mod = reload(sys.modules[module_name])
            else:
                mod = __import__(module_name)
            class_ = getattr(mod, class_name)
            return class_()
        except ImportError:
            print 'can not load module %s' % str(module_name)