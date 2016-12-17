#!/usr/bin/python
"""Imports"""
from flask import Flask
from flask import render_template
from movement import Movement as Move
from turn import Turn

APP = Flask(__name__)


@APP.route("/")
def index():
    """ the index route """
    return render_template('index.html')


@APP.route("/car/forward/<int:seconds>")
def forward(seconds):
    """forward method"""
    move_fwd = Move()
    move_fwd.forward(seconds)
    return "done", seconds


@APP.route("/car/backward/<int:seconds>")
def backward(seconds):
    """backward method"""
    move_bwd = Move()
    move_bwd.backward(seconds)
    return "done", seconds


@APP.route("/car/left/<int:seconds>")
def left(seconds):
    """left method"""
    turn_lft = Turn()
    turn_lft.left(seconds)
    return "done", seconds


@APP.route("/car/right/<int:seconds>")
def right(seconds):
    """right method"""
    turn_rgt = Turn()
    turn_rgt.right(seconds)
    return "done", seconds


# @APP.route("/status/")
# @APP.route("/status/<int:pin_id>")
# def status(pin_id=None):
#     """ a status"""
#     if not pin_id:
#         return "none"
#     else:
#         return "status pin %s" % (pin_id)


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=8020, debug=True)
