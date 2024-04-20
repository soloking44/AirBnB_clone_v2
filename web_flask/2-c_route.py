#!/usr/bin/python3
""" this initialzes application """
from flask import Flask
res = Flask(__name__)


@res.route('/', strict_slashes=False)
def fun():
    """ this outputs a msg when / is invoked """
    return 'Hello HBNB!'


@res.route('/hbnb', strict_slashes=False)
def fun2():
    """ this outputs a msg when /hbnb is invoked """
    return 'HBNB'


@res.route('/c/<text>', strict_slashes=False)
def fun3(text):
    """ this outputs a msg when /c is invoked """
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    """ this is the fun """
    res.run(host='0.0.0.0', port=5000)
