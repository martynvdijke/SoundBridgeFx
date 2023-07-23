
import json
from flask import jsonify, request
from soundbridgefx import web_backend
from soundbridgefx.AbstractSpeaker import speaker

app = web_backend.app
Speakers = speaker.AbstractSpeaker()
Speakers.add_sonos_controller()

@app.route("/api/v1/speakers/all", methods=["GET"])
def get_all_speakers():
    return Speakers.get_all_speakers()


@app.route("/api/v1/speakers/play/stream", methods=["POST"])
def play_stream():
    record = json.loads(request.data)
    response = Speakers.play(record["selected"])
    return jsonify(response)


@app.route("/api/v1/speakers/play/stream", methods=["POST"])
def play_party():
    record = json.loads(request.data)
    response = Speakers.party_mode(record["selected"])
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