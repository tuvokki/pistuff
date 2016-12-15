#!/usr/bin/python

"""Import modules"""
import logging
import argparse
from movement import Movement as Move
from turn import Turn

logging.basicConfig(format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

# help info
PARSER = argparse.ArgumentParser(description='Laat de auto rijden.')
# PARSER.add_argument('--loglevel', help='log alles', default='info')
PARSER.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
PARSER.add_argument(
    '--direction', help='Set to 1 for clockwise and -1 for anti-clockwise', type=int, default=1)
PARSER.add_argument(
    '--seconds', help='How long must the car drive', type=int, default=1)
PARSER.add_argument(
    '--speed', help='How fast must the car drive', type=int, default=1)
ARGS = PARSER.parse_args()
# LOGLEVEL = ARGS.loglevel
DIRECTION = ARGS.direction
DIRECTION = -1  # backward
DRIVE_TIME = ARGS.seconds
WAIT_TIME = ARGS.speed / float(1000)

# set log level
if ARGS.verbose:
    logging.getLogger().setLevel(logging.DEBUG)

AMOVE = Move()
AMOVE.drive_time = 2
AMOVE.run()

ATURN = Turn()
ATURN.drive_time = 2
ATURN.direction = -1
ATURN.run()

AMOVE = Move()
AMOVE.wait_time = 5
AMOVE.run()
