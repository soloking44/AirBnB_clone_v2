#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
res = Flask(__name__)


@res.route('/', strict_slashes=False)
def fun():
    """this is Hello HBNB!"""
    return 'Hello HBNB!'


@res.route('/hbnb', strict_slashes=False)
def fun2():
    """this is HBNB"""
    return 'HBNB'


@res.route('/c/<text>', strict_slashes=False)
def fun3(text):
    """this shows C and text var"""
    return 'C ' + text.replace('_', ' ')


@res.route('/python', strict_slashes=False)
@res.route('/python/<text>', strict_slashes=False)
def fun4(text='is cool'):
    """this shows python and text var"""
    return 'Python ' + text.replace('_', ' ')


@res.route('/number/<int:n>', strict_slashes=False)
def fun5(n):
    """this shows n only if n is an int"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    res.run(host='0.0.0.0', port='5000')

