
import json
from flask import jsonify, request
from soundbridgefx import cvlc, backend

app = backend.app
CVLC = cvlc.CLV()

##TODO refactor

@app.route("/api/v1/stream/speakers", methods=["POST"])
def get_all_stream_speakers():
    record = json.loads(request.data)
    response = CVLC
    return jsonify(response)

@app.route("/api/v1/stream/microphones", methods=["POST"])
def get_all_stream_microphone():
    record = json.loads(request.data)
    response = CVLC
    return jsonify(response)

@app.route("/api/v1/stream/speaker", methods=["POST"])
def get_all_stream_speaker():
    record = json.loads(request.data)
    response = CVLC
    return jsonify(response)

app.route("/api/v1/stream/microphone", methods=["POST"])
def get_stream_microphone():
    record = json.loads(request.data)
    response = CVLC
    return jsonify(response)

@app.route("/api/v1/stream/speaker", methods=["POST"])
def get_stream_speaker():
    record = json.loads(request.data)
    response = CVLC
    return jsonify(response)

app.route("/api/v1/stream/microphone", methods=["POST"])
def set_stream_microphone():
    record = json.loads(request.data)
    response = CVLC
    return jsonify(response)

app.route("/api/v1/stream/speaker", methods=["POST"])
def set_stream_speaker():
    record = json.loads(request.data)
    response = CVLC
    return jsonify(response)
