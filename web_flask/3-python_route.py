#!/usr/bin/python3
"""this intialize web application
"""

from flask import Flask
res = Flask(__name__)


@res.route('/', strict_slashes=False)
def fun():
    """this echoes Hello HBNB!"""
    return 'Hello HBNB!'


@res.route('/hbnb', strict_slashes=False)
def fun2():
    """this echoes HBNB"""
    return 'HBNB'


@res.route('/c/<text>', strict_slashes=False)
def fun3(text):
    """this outputs C and text var"""
    return 'C ' + text.replace('_', ' ')


@res.route('/python', strict_slashes=False)
@res.route('/python/<text>', strict_slashes=False)
def fun4(text='is cool'):
    """this outputs python and text var"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    res.run(host='0.0.0.0', port='5000')
