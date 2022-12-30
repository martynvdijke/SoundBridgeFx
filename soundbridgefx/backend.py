from flask import Flask, jsonify, send_from_directory
import json
import random
import jsonpickle

from soundbridgefx import (
    speakers
)
app = Flask(__name__)
Speakers = speakers.Speakers()

# # Path for our main Svelte page
# @app.route("/")
# def base():
#     return send_from_directory('client/public', 'index.html')

# # Path for all the static files (compiled JS/CSS, etc.)
# @app.route("/<path:path>")
# def home(path):
#     return send_from_directory('client/public', path)

@app.route("/api/speakers")
def get_all_speakers():
    return jsonpickle.encode(Speakers)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

def main():
    # Run the app server on localhost:4449
    app.run('localhost', 4449)
