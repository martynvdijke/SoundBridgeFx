
import json
from flask import jsonify, request
from soundbridgefx import speakers, backend

app = backend.app
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