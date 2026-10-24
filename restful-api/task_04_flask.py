#!/usr/bin/python3
"""A simple Flask API that stores users in memory."""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Returns a welcome message for the root URL."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Returns the list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns OK to show that the API is running."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full user object for the given username."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user from the JSON body of the request."""
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
