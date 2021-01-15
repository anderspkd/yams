from flask import Flask, request, redirect, jsonify
from util import *
app = Flask(__name__)


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.route("/play", methods=["POST"])
def play():
    add_song(request.form["link"])
    return redirect("/")


@app.route("/play_existing", methods=["POST"])
def play_existing():
    return play_song(int(request.form("index")))


@app.route("/stop")
def stop():
    stop_song()


@app.route("/pause_or_resume")
def pause_or_resume():
    pause_or_resume_song()


@app.route("/playing")
def playing():
    return jsonify(SONGS)
