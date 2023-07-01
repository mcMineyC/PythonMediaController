from flask import Flask, send_from_directory
from pynput.keyboard import Key, Controller
kbd = Controller()

app = Flask(__name__)

@app.route("/")
def root():
    return send_from_directory('.', "index.html")
@app.route("/prev")
def prev():
    kbd.press(Key.media_previous)
    kbd.release(Key.media_previous)
    return "1"
@app.route("/plause")
def playpause():
    kbd.press(Key.media_play_pause)
    kbd.release(Key.media_play_pause)
    return "1"
@app.route("/next")
def next():
    kbd.press(Key.media_next)
    kbd.release(Key.media_next)
    return "1"
app.run(host="0.0.0.0",port="6541",debug=True)