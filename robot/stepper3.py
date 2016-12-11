#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
STEP_PINS = [19, 20, 21, 26]
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

# Initialise variables
STEP_COUNTER = 0

# Start main loop
try:
    while True:

        print STEP_COUNTER,
        print SEQ[STEP_COUNTER]

        for pin in range(0, 4):
            xpin = STEP_PINS[pin]  # Get GPIO
            if SEQ[STEP_COUNTER][pin] != 0:
                print " Enable GPIO %i" % (xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        STEP_COUNTER += STEP_DIR

        # If we reach the end of the sequence
        # start again
        if STEP_COUNTER >= STEP_COUNT:
            STEP_COUNTER = 0
        if STEP_COUNTER < 0:
            STEP_COUNTER = STEP_COUNT + STEP_DIR

        # Wait before moving on
        time.sleep(WAIT_TIME)

except KeyboardInterrupt:
    # GPIO netjes afsluiten
    GPIO.cleanup()
