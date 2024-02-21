#!/usr/bin/env python3
"""App module"""
from flask import Flask, jsonify

app = __name__(Flask)


@app.route("/", methods=['GET'])
def welcome():
    """Welcome message"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
