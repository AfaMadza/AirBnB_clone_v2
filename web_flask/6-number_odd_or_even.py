#!/usr/bin/python3
"""
This module contains a function that starts a Flask web app
"""
from flask import render_template
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
    """
    Returns specified text response based on optional parameter
    """
    new_str = text.replace("_", " ")
    return 'Python %s' % new_str


@app.route('/number/<int:n>')
def isnumber(n):
    """
    Returns response if parameter passed is an int
    """
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def numtemp(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def evenodd(n):
    if n % 2 == 0:
        data = 'even'
    else:
        data = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
