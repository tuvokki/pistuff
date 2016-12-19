#!/usr/bin/python
"""Imports"""
from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin
from movement import Movement as Move
from turn import Turn

APP = Flask(__name__)
CORS(APP, resources={r"/car/*": {"origins": "*"}})


@APP.route("/")
def index():
    """ the index route """
    return render_template('index.html')


@cross_origin()
@APP.route("/car/<string:direction>/<int:seconds>", methods=['POST', 'OPTIONS'])
def move(direction, seconds):
    """generic move method"""
    if direction in ['forward', 'backward']:
        exec_move = Move()
        if direction == 'forward':
            exec_move.forward(seconds)
        else:
            exec_move.backward(seconds)
        result = 'done move'
    elif direction in ['left', 'right']:
        exec_move = Turn()
        if direction == 'left':
            exec_move.left(seconds)
        else:
            exec_move.right(seconds)
        result = 'done turn'
    else:
        result = '{0} is no valid direction, choose between forward, backward, left, right.'.format(
            direction)
    return jsonify({'result': result, 'direction': direction, 'seconds':
                    seconds})


@APP.route("/car/forward/<int:seconds>", methods=['GET'])
def forward(seconds):
    """forward method"""
    move_fwd = Move()
    move_fwd.forward(seconds)
    return jsonify({'result': "done", 'direction': '', 'drive_time': seconds})


@APP.route("/car/backward/<int:seconds>", methods=['GET'])
def backward(seconds):
    """backward method"""
    move_bwd = Move()
    move_bwd.backward(seconds)
    return jsonify({'result': "done", 'direction': '', 'drive_time': seconds})


@APP.route("/car/left/<int:seconds>", methods=['GET'])
def left(seconds):
    """left method"""
    turn_lft = Turn()
    turn_lft.left(seconds)
    return jsonify({'result': "done", 'direction': '', 'drive_time': seconds})


@APP.route("/car/right/<int:seconds>", methods=['GET'])
def right(seconds):
    """right method"""
    turn_rgt = Turn()
    turn_rgt.right(seconds)
    return jsonify({'result': "done", 'direction': '', 'drive_time': seconds})


# @APP.route("/status/")
# @APP.route("/status/<int:pin_id>")
# def status(pin_id=None):
#     """ a status"""
#     if not pin_id:
#         return "none"
#     else:
#         return "status pin %s" % (pin_id)


# if __name__ == "__main__":
#     APP.run(host='0.0.0.0', port=8020, debug=True)
