#!/usr/bin/python
from flask import Flask
from flask import render_template
import json
import RPi.GPIO as GPIO

app = Flask(__name__)

activeleds = [12,24]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def togglepin(pin):
  if GPIO.input(pin):
    GPIO.output(pin, GPIO.LOW)
  else:
    GPIO.output(pin, GPIO.HIGH)

def getstatus():
  status = {}
  for led in activeleds:
    GPIO.setup(led, GPIO.OUT)
    status[led] = GPIO.input(led)
  return [status]

@app.route("/")
def hello():
  ledstatus = getstatus()
  return render_template('hello.html', ledstatus=ledstatus)

@app.route("/toggle/<int:pin_id>")
def toggle(pin_id):
  if pin_id in activeleds:
    GPIO.setup(pin_id, GPIO.OUT)
    togglepin(pin_id)
    pin_status = GPIO.input(pin_id)
    return "toggeling %s, set to %s" % (pin_id, pin_status)
  else:
    return "only pins 12 and 24 are connected"

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=80,debug=True)
