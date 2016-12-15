""" Imports """
import logging
import threading
import time
import RPi.GPIO as GPIO


class Turn(object):
    """ Turn class """
    STEP_PINS_RIGHT = [19, 20, 21, 26]
    STEP_PINS_LEFT = [17, 22, 23, 24]

    def __init__(self):
        logging.basicConfig(
            format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

        self.direction = 1  # forward
        self.drive_time = 1  # seconds
        self.wait_time = 10 / float(100)  # speedunit

    def worker(self, pins, waittime, move_dir):
        """ The worker """
        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)

        # Define advanced sequence
        # as shown in manufacturers datasheet
        seq = [[1, 0, 0, 1],
               [1, 0, 0, 0],
               [1, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 1, 1],
               [0, 0, 0, 1]]

        step_count = len(seq)
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
            logging.debug(seq[counter])

            for pin in range(0, 4):
                xpin = pins[pin]  # Get GPIO
                if seq[counter][pin] != 0:
                    logging.debug('Enable GPIO %i', xpin)
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

            counter += move_dir

            # If we reach the end of the sequence
            # start again
            if counter >= step_count:
                counter = 0
            if counter < 0:
                counter = step_count + move_dir

            # Wait before moving on
            time.sleep(waittime)

    def run(self):
        """The run method"""
        right_thread = threading.Thread(
            name='right_wheel',
            target=self.worker,
            args=(self.STEP_PINS_RIGHT, self.wait_time, self.direction,))
        left_thread = threading.Thread(
            name='left_wheel',
            target=self.worker,
            args=(self.STEP_PINS_LEFT, self.wait_time, self.direction,))

        # Start main loop
        try:
            right_thread.start()
            left_thread.start()
            # laat x seconden rijden
            time.sleep(self.drive_time)
            # threads opruimen
            right_thread.do_run = False
            right_thread.join()
            left_thread.do_run = False
            left_thread.join()
            # GPIO netjes afsluiten
            GPIO.cleanup()

        except (KeyboardInterrupt, SystemExit):
            # GPIO netjes afsluiten
            GPIO.cleanup()
