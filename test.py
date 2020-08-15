# test.py

from flask import Flask

app = Flask(__name__)


@app.route('/')
def test():
    return "Music Management App"
