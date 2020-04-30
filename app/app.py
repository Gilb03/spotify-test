from flask import Flask
import index
import playlist

app = Flask(__name__)

@app.route('/')
def playlist():
    return index

@app.route('/playlist')
def playlist():
    return playlist
