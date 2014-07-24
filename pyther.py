#!/usr/bin/env python
"""
small, expandable python based login shell

Written by DerCoop <dercoop@users.sourceforge.net>

"""

__author__ = 'coop'
__license__ = 'GPLv2'

import sys
import os
import pyther.module_loader as module_loader
import pyther.misc as misc
from pyther.Pyther import Pyther


def get_cli_options():
    '''parse command line options'''
    import optparse
    """returns a pair (values, args) of the command line options"""
    parser = optparse.OptionParser(usage=optparse.SUPPRESS_USAGE)
    parser.add_option('--loglevel', action='store',
                      help='<critical | error | warning | info | debug | notset>')
    parser.add_option('--config-file', action='store',
                      help='the name of the configfile')
    parser.add_option('--path', action='store',
                      help='the plugin path')

    return parser.parse_args()


def __getln():
    '''parse a line from stdin until a newline'''
    return str(sys.stdin.readline()).strip()


def run_shell(modules, path):
    '''start the shell in an atomloop until the keyword 'quit' is typed

    :param modules: all known modules (found in paths folder)
    :param path:    the folder to parse for modules
    '''
    # read until newline
    loader = module_loader.Loader(path)
    lines = __getln()
    while not lines == 'quit':
        line = lines.split(' ', 1)
        cmd = line[0]
        if len(line) > 1:
            args = line[1]
        else:
            args = None

        if cmd in modules:
            command = loader.load(cmd, cmd.title())
            command.run(args)
        else:
            print 'unknown command: %s' % cmd

        lines = __getln()


def main():
    '''parse the default config and start the shell

    :return:
    0:  on success
    1:  on failure
    '''
    opts, args = get_cli_options()

    cfg = ''
    if opts.config_file:
        configfile = opts.config_file
        if not os.path.isfile(configfile):
            msg = 'config file did not exist (' + configfile + ')'
            misc.die(-1, msg)
        raise NotImplementedError('This option is not implemented at the moment')
        #cfg = parse_config(configfile)

    if opts.loglevel:
        raise NotImplementedError('This option is not implemented at the moment')

    if opts.path:
        path = opts.path
    else:
        misc.die(1, 'define a plugin path')

    # add default plugin static
    sys.path.insert(0, 'pyther')
    #known_modules = ['plugin']
    known_modules = []

    for plugin in os.listdir(path):
        pname, ext = os.path.splitext(plugin)
        if pname == '__init__':
            continue
        if ext == '.py':
            known_modules.append(pname)

    # TODO add manpage
    # TODO add completion
    # TODO add history

    pyther = Pyther(known_modules, path)
    pyther.prompt = 'pyther# '
    pyther.cmdloop('Welcome to PytherShell')

    #run_shell(known_modules, path)
    misc.die(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        misc.die(0, 'aborted by user')
