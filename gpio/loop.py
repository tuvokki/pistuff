#!/usr/bin/python
# importeer argparse om commandline argumenten te lezen
import argparse, logging
# importeer de GPIO bibliotheek.
import RPi.GPIO as GPIO
# Importeer de time biblotheek voor tijdfuncties.
from time import sleep

# help info
parser = argparse.ArgumentParser(description='Laat het rondje lopen.')
# parser.add_argument('waittime', type=float, help='aan/uit tijd (bijvoorbeeld 0.3)', default=0.3)
# parser.add_argument('pin', help='GPIO pin nummer', type=int)
parser.add_argument('-v', '--verbose', help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()

pins = [20,21,23,18,24,16]

# set log level
if (args.verbose):
  logging.basicConfig(level=logging.DEBUG)
else:
  logging.basicConfig(level=logging.INFO)

# Deze methode kijkt of de pin hoog of laag is, en draait dat om
def togglepin(pin):
  if GPIO.input(pin):
    logging.debug('Zet de pin ' + str(pin) + ' uit/0/false.')
    GPIO.output(pin, GPIO.LOW)
  else:
    logging.debug('Zet de pin ' + str(pin) + ' aan/1/true.')
    GPIO.output(pin, GPIO.HIGH)

# De main loop van het programma
def main():

  # set variabelen
  # ledpin = args.pin
  # waittime = args.waittime
  waittime = 0.3
  # logging.info('Knipper led op pin: ' + str(ledpin))
  logging.debug('met interval: ' + str(waittime))

  # Zet de pinmode op Broadcom SOC.
  GPIO.setmode(GPIO.BCM)
  # Zet waarschuwingen uit.
  GPIO.setwarnings(False)

  # Zet de GPIO pins als uitgang.
  for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

  try:
    while True:
      # toggle de led.
      for pin in pins:
        togglepin(pin)
        # Wacht waittime seconde.
        sleep(waittime)

  except KeyboardInterrupt:
    # GPIO netjes afsluiten.
    logging.info('Stop programma')
    GPIO.cleanup()

# run de main loop van het programma
if __name__ == "__main__":
   main()
