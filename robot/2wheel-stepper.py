#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

DEBUG = False

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

LEFT_PINS = [17, 22, 23, 24]
RGHT_PINS = [19, 20, 21, 26]

# Set all pins as output
for pin in RGHT_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
for pin in LEFT_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

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
STEP_LEFT = -1  # Set to 1 or 2 for clockwise
STEP_RGHT = 1  # Set to 1 or 2 for clockwise
# Set to -1 or -2 for anti-clockwise

# Read wait time from command line
if len(sys.argv) > 1:
    WAIT_TIME = int(sys.argv[1]) / float(1000)
else:
    WAIT_TIME = 10 / float(1000)

# Initialise variables
LEFT_COUNTER = 0
RGHT_COUNTER = 0

# Start main loop
try:
    while True:
        if DEBUG:
            print LEFT_COUNTER,
            print SEQ[LEFT_COUNTER]
        print "Rolling left"
        for pin in range(0, 4):
            xpin = LEFT_PINS[pin]  # Get GPIO
            if SEQ[LEFT_COUNTER][pin] != 0:
                if DEBUG:
                    print " Enable GPIO %i" % (xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        LEFT_COUNTER += STEP_LEFT

        # If we reach the end of the sequence
        # start again
        if LEFT_COUNTER >= STEP_COUNT:
            LEFT_COUNTER = 0
        if LEFT_COUNTER < 0:
            LEFT_COUNTER = STEP_COUNT + STEP_LEFT

        if DEBUG:
            print RGHT_COUNTER,
            print SEQ[RGHT_COUNTER]
        print "Rolling right"
        for pin in range(0, 4):
            xpin = RGHT_PINS[pin]  # Get GPIO
            if SEQ[RGHT_COUNTER][pin] != 0:
                if DEBUG:
                    print " Enable GPIO %i" % (xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        RGHT_COUNTER += STEP_RGHT

        # If we reach the end of the sequence
        # start again
        if RGHT_COUNTER >= STEP_COUNT:
            RGHT_COUNTER = 0
        if RGHT_COUNTER < 0:
            RGHT_COUNTER = STEP_COUNT + STEP_RGHT

        # Wait before moving on
        print "Waiting for {}".format(WAIT_TIME)
        time.sleep(WAIT_TIME)

except KeyboardInterrupt:
    # GPIO netjes afsluiten
    GPIO.cleanup()
