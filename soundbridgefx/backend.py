from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

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
    app.run("localhost", 4449)
