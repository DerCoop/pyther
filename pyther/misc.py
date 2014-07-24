"""
misc functions for pyther

Written by DerCoop <dercoop@users.sourceforge.net>

"""
__author__ = 'coop'
__license__ = 'GPLv2'


def die(rc, message=None):
    """print message and exit

    Note: This function uses the logging packet, if this is not configured
        use "print(message)" instead

    Arguments:
    rc:         returncode
    message:    log message
    """
    import sys

    if message:
        #log.error(message)
        print message
    sys.exit(rc)


