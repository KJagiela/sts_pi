import os

from flask import Flask, render_template, jsonify, request
from jinja2 import Template

# import explorerhat as eh

app = Flask(__name__)


# ugh globals - how to fix these?
speed_right = 0
speed_left = 0


@app.route('/hello')
def hello():
    return render_template(
        'template.html',
        speed_right=speed_right,
        speed_left=speed_left,
    )


@app.route('/steer', methods=['POST'])
def steer():
    global speed_left
    global speed_right
    pressed_key = request.json.get('pressed_key')
    if pressed_key == 'ArrowUp':
        speed_right += 10
        speed_left += 10
    elif pressed_key == 'ArrowDown':
        speed_right -= 10
        speed_left -= 10
    elif pressed_key == 'ArrowRight':
        speed_right += 5
        speed_left -= 5
    elif pressed_key == 'ArrowLeft':
        speed_right -= 5
        speed_left += 5
    speed_left = min(max(speed_left, -100), 100)
    speed_right = min(max(speed_right, -100), 100)
    # eh.motor.one.speed(speed_right)
    # eh.motor.two.speed(speed_left)
    return jsonify({'speed_right': speed_right, 'speed_left': speed_left})
