#!/usr/bin/python
from flask import Flask
from flask import render_template
import json
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def togglepin(pin):
  if GPIO.input(pin):
    GPIO.output(pin, GPIO.LOW)
  else:
    GPIO.output(pin, GPIO.HIGH)

def getstatus():
  # return [{'led': 12, 'status': GPIO.input(12)}, {'led': 24, 'status': GPIO.input(24)}]
  return [{12: GPIO.input(12), 24: GPIO.input(24)}]

@app.route("/")
def hello():
  GPIO.setup(12, GPIO.OUT)
  GPIO.setup(24, GPIO.OUT)
  ledstatus = getstatus()
  return render_template('hello.html', ledstatus=ledstatus)

@app.route("/toggle/<int:pin_id>")
def toggle(pin_id):
  if pin_id == 12 or pin_id == 24:
    GPIO.setup(pin_id, GPIO.OUT)
    togglepin(pin_id)
    pin_status = GPIO.input(pin_id)
    return "toggeling %s, set to %s" % (pin_id, pin_status)
  else:
    return "only pins 12 and 24 are connected"

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=80,debug=True)
