from flask import Flask, request, redirect, jsonify
from util import *
app = Flask(__name__)


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.route("/play", methods=["POST"])
def play():
    add_song(request.form['link'])
    return redirect("/")


@app.route("/stop")
def stop():
    pass


@app.route("/pause")
def pause():
    pass


@app.route("/playing")
def playing():
    return jsonify(SONGS)
