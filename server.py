from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "No songs playing"

@app.route("/play")
def play():
    pass

@app.route("/stop")
def stop():
    pass

@app.route("/pause")
def pause():
    pass
