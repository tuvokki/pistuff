#!/usr/bin/python

# importeer de GPIO bibliotheek.
import RPi.GPIO as GPIO
# Importeer de time biblotheek voor tijdfuncties.
from time import sleep

# Zet de pinmode op Broadcom SOC.
GPIO.setmode(GPIO.BCM)
# Zet waarschuwingen uit.
GPIO.setwarnings(False)
# Stel de GPIO pinnen in voor de stappenmotor:
# StepPins = [21,20,16,12]
StepPins = [17,22,23,24]

# Set alle pinnen als uitgang.
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

# Definieer variabelen.
StepCounter = 0

# Definieer simpele volgorde
StepCount1 = 4
Seq1 = []
Seq1 = range(0, StepCount1)
Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]

# Definieer geadvanceerde volgorde (volgens de datasheet)
StepCount2 = 8
Seq2 = []
Seq2 = range(0, StepCount2)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

# Welke stappenvolgorde gaan we hanteren?
Seq = Seq2
StepCount = StepCount2

try:
  while True:
    for pin in range(0, 4):
      xpin = StepPins[pin]
      if Seq[StepCounter][pin]!=0:
        print "Stap: %i GPIO Actief: %i" %(StepCounter,xpin)
        GPIO.output(xpin, True)
      else:
        GPIO.output(xpin, False)

    StepCounter += 1

    # Als we aan het einde van de stappenvolgorde zijn beland start dan opnieuw
    if (StepCounter==StepCount): StepCounter = 0
    if (StepCounter<0): StepCounter = StepCount

    # Wacht voor de volgende stap (lager = snellere draaisnelheid)
    sleep(.0005)

except KeyboardInterrupt:
  # GPIO netjes afsluiten
  GPIO.cleanup()
