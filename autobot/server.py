#!/usr/bin/python
"""Imports"""
from flask import Flask
from flask import render_template
import movement

APP = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


@APP.route("/")
def hello():
    """ the index route """
    return render_template('index.html')


@APP.route("/forward/<int:waittime>/<int:number>")
def walker(waittime, number):
    """walker method"""
    return "done", waittime, number


@APP.route("/status/")
@APP.route("/status/<int:pin_id>")
def status(pin_id=None):
    """ a status"""
    if not pin_id:
        return "none"
    else:
        return "status pin %s" % (pin_id)


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=8020, debug=True)
