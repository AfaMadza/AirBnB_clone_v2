#!/usr/bin/python3
"""
This module contains a function that starts a Flask web app
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    Returns a specific response
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Returns a specific response
    """
    return 'HBNB'


@app.route('/c/<text>')
def cisfun(text):
    """
    Returns specified text response
    """
    new_str = text.replace("_", " ")
    return 'C %s' % new_str

@app.route('/python')
@app.route('/python/<text>')
def pycool(text="is cool"):
    new_str = text.replace("_", " ")
    return 'Python %s' % new_str


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
