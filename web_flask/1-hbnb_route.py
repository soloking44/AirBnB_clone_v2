#!/usr/bin/python3
""" this initialize flask for HBNB app
"""
from flask import Flask
res = Flask(__name__)


@res.route('/', strict_slashes=False)
def fun():
    """ this outputs a response when / is invoked """
    return 'Hello HBNB!'


@res.route('/hbnb', strict_slashes=False)
def fun2():
    """ this outputs a response when /hbnb is invoked """
    return 'HBNB'

if __name__ == "__main__":
    """ this is the function """
    res.run(host='0.0.0.0', port=5000)
