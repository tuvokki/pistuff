#!/usr/bin/python

"""
Import modules
"""
import sys
import logging
import threading
import time
import argparse
import RPi.GPIO as GPIO

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

# help info
PARSER = argparse.ArgumentParser(description='Laat de auto rijden.')
PARSER.add_argument('loglevel', help='log alles', default='info')
PARSER.add_argument(
    'direction', help='Set to 1 for clockwise and -1 for anti-clockwise', type=int, default=1)
ARGS = PARSER.parse_args()
LOGLEVEL = ARGS.loglevel

# set log level
getattr(logging, LOGLEVEL.upper())

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

STEP_PINS_RIGHT = [19, 20, 21, 26]
STEP_PINS_LEFT = [17, 22, 23, 24]

# Define advanced sequence
# as shown in manufacturers datasheet
SEQ = [[1, 0, 0, 1],
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1]]

STEP_COUNT = len(SEQ)
STEP_DIR = 1  # Set to 1 or 2 for clockwise
# Set to -1 or -2 for anti-clockwise

# Read wait time from command line
if len(sys.argv) > 1:
    WAIT_TIME = int(sys.argv[1]) / float(1000)
else:
    WAIT_TIME = 10 / float(1000)


def worker(pins, waittime, direction):
    """ The worker """
    logging.info('Starting thread')
    cur_thr = threading.currentThread()

    # Set all pins as output
    for pin in pins:
        logging.debug('Setup pins')
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)
    counter = 0
    while getattr(cur_thr, "do_run", True):

        logging.debug(counter)
        logging.debug(SEQ[counter])

        for pin in range(0, 4):
            xpin = pins[pin]  # Get GPIO
            if SEQ[counter][pin] != 0:
                logging.debug('Enable GPIO %i', xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        counter += direction

        # If we reach the end of the sequence
        # start again
        if counter >= STEP_COUNT:
            counter = 0
        if counter < 0:
            counter = STEP_COUNT + direction

        # Wait before moving on
        time.sleep(waittime)


RIGHT_THREAD = threading.Thread(
    name='right_wheel', target=worker, args=(STEP_PINS_RIGHT, WAIT_TIME, 1,))
LEFT_THREAD = threading.Thread(
    name='left_wheel', target=worker, args=(STEP_PINS_LEFT, WAIT_TIME, -1,))

# Start main loop
try:
    RIGHT_THREAD.start()
    LEFT_THREAD.start()
    # laat 5 seconden rijden
    time.sleep(5)
    # threads opruimen
    RIGHT_THREAD.do_run = False
    RIGHT_THREAD.join()
    LEFT_THREAD.do_run = False
    LEFT_THREAD.join()
    # GPIO netjes afsluiten
    GPIO.cleanup()


except (KeyboardInterrupt, SystemExit):
    # GPIO netjes afsluiten
    GPIO.cleanup()
