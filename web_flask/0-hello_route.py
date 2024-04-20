#!/usr/bin/python3
"""
this is the beginning of flask
"""

from flask import Flask
res = Flask(__name__)


@res.route('/', strict_slashes=False)
def fun():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    res.run(host='0.0.0.0', port='5000')
