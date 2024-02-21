#!/usr/bin/env python3
"""App module"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def welcome():
    """Welcome message"""
    return jsonify({"message": "Hello World!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
