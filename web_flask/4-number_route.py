#!/usr/bin/python3
"""
this initialze flask app
"""

from flask import Flask
res = Flask(__name__)


@res.route('/', strict_slashes=False)
def fun():
    """echoes Hello HBNB!"""
    return 'Hello HBNB!'


@res.route('/hbnb', strict_slashes=False)
def fun2():
    """echoes HBNB"""
    return 'HBNB'


@res.route('/c/<text>', strict_slashes=False)
def fun3(text):
    """this shows C and text var"""
    return 'C ' + text.replace('_', ' ')


@res.route('/python', strict_slashes=False)
@res.route('/python/<text>', strict_slashes=False)
def fun4(text='is cool'):
    """this dhows python and text var"""
    return 'Python ' + text.replace('_', ' ')


@res.route('/number/<int:n>', strict_slashes=False)
def fun5(n):
    """this shoes n as num when n is an integer"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    res.run(host='0.0.0.0', port='5000')
