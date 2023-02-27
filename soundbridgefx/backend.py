from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
from soundbridgefx import speakers

app = Flask(__name__)
CORS(app)
Speakers = speakers.Speakers()

@app.route("/api/v1/speakers/all", methods=["GET"])
def get_all_speakers():
    return Speakers.get_all_speakers()


@app.route("/api/v1/speakers/play/stream", methods=["POST"])
def play_stream():
    record = json.loads(request.data)
    response = Speakers.play_stream(record["selected"])
    return jsonify(response)


@app.route("/api/v1/speakers/play/stream", methods=["POST"])
def play_party():
    record = json.loads(request.data)
    response = Speakers.play_party(record["selected"])
    return jsonify(response)


@app.route("/api/v1/speakers/stop", methods=["POST"])
def stop():
    record = json.loads(request.data)
    response = Speakers.stop(record["selected"])
    return jsonify(response)


@app.route("/api/v1/v1/speakers/pause", methods=["POST"])
def pause():
    record = json.loads(request.data)
    response = Speakers.pause(record["selected"])
    return jsonify(response)


@app.route("/api/v1/speakers/volume", methods=["POST"])
def set_volume():
    record = json.loads(request.data)
    response = Speakers.set_volume(record["selected"])
    return jsonify(response)



"""Main route for serving the web app

Returns:
    _type_: _description_
"""
@app.route("/")
def base():
    return send_from_directory("web/prerendered/pages", "index.html")


"""Assets url

Returns:
    _type_: _description_
"""
@app.route("/<path:path>")
def home(path):
    return send_from_directory("web/client", path)

def main():
    # Run the app server on localhost:4449
    print(app.url_map)
    app.run("localhost", 4449)
