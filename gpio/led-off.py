#!/usr/bin/python
# importeer argparse om commandline argumenten te lezen
import argparse
# importeer de GPIO bibliotheek.
import RPi.GPIO as GPIO

# help info
parser = argparse.ArgumentParser(description='Zet een lampje uit.')
parser.add_argument('pin', help='GPIO pin nummer', type=int)
args = parser.parse_args()

def main():
  ledpin = args.pin

  # Zet de pinmode op Broadcom SOC.
  GPIO.setmode(GPIO.BCM)
  # Zet waarschuwingen uit.
  GPIO.setwarnings(False)

  # Zet de GPIO pin als uitgang.
  GPIO.setup(ledpin, GPIO.OUT)

  # Zet de LED aan.
  GPIO.output(ledpin, GPIO.LOW)

# run de main loop van het programma
if __name__ == "__main__":
   main()
