"""
example plugin for pyther

This is a short example how to use pyther plugins
"""
__author__ = 'coop'

import sys
import shlex
from plugin import Plugin


class Cat(Plugin):
    def __init__(self):
        pass

    @staticmethod
    def __get_cli_options(args):
        '''parse command line options'''
        import optparse
        """returns a pair (values, args) of the command line options"""
        parser = optparse.OptionParser(usage=optparse.SUPPRESS_USAGE)
        parser.add_option('-n', '--line-number', action='store_true',
                          help='show line numbers')

        return parser.parse_args(args=shlex.split(args))

    @staticmethod
    def __print_file(filename, show_linenumbers):
        '''print the file to stdout

        :param filename:            the name of the fle to print
        :param show_linenumbers:    show line numbers
        '''

        try:
            with open(filename, 'r') as fd:
                ln = 1
                # read line by line, fast and memory efficient
                for line in fd:
                    if show_linenumbers:
                        sys.stdout.write(str(ln) + '\t')
                    # print w/o leading newline
                    sys.stdout.write(line)
                    ln += 1
        except IOError:
            msg = 'Can\'t read file: ' + str(filename) + '\n'
            sys.stderr.write(msg)

    def run(self, args):
        if not args:
            print('no file given')
            return
        opt, arg = self.__get_cli_options(args)

        if not arg:
            print 'no file given'
            return

        for f in arg:
            self.__print_file(f, opt.line_number)
            return
