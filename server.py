from dataclasses import dataclass
from threading import Thread
import unicodedata as ud
import json
import math
import time

import eventlet
from flask_socketio import SocketIO
from flask import Flask, send_from_directory, render_template

from ip import ip_address, port

async_mode = None
app = Flask(__name__, static_url_path='')
socketio = SocketIO(app, async_mode=async_mode)



# Main page
@app.route('/')
def root():
    return render_template('main.html')


# Get files from server (etc. libs)
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@socketio.on('keyup')
def up(data):
    username = data['user']
    print('key pressed')


@socketio.on('keydown')
def down(data):
    print('key unpressed')


# We start a parallel thread for game logics. This loop is constantly running 
# def game_loop(name):
#     while True:
#         # Process game logic here if you need to

#         time.sleep(0.01)


if __name__ == "__main__":
    eventlet.monkey_patch()

    # x = Thread(target=game_loop, args=(1,))
    # x.start()
    
    print(f'Listening on http://{ip_address}:{port}')
    socketio.run(app, host=ip_address, port=port)
