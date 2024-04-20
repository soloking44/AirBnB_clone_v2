#!/usr/bin/python3
"""
flask app
"""

from flask import Flask, render_template
res = Flask(__name__)


@res.route('/', strict_slashes=False)
def fun():
    """Hello HBNB!"""
    return 'Hello HBNB!'


@res.route('/hbnb', strict_slashes=False)
def fun1():
    """HBNB"""
    return 'HBNB'


@res.route('/c/<text>', strict_slashes=False)
def fun2(text):
    """shows C and text var"""
    return 'C ' + text.replace('_', ' ')


@res.route('/python', strict_slashes=False)
@res.route('/python/<text>', strict_slashes=False)
def fun3(text='is cool'):
    """shows py and text var"""
    return 'Python ' + text.replace('_', ' ')


@res.route('/number/<int:n>', strict_slashes=False)
def fun4(n):
    """shows n when n is an int"""
    return "{:d} is a number".format(n)


@res.route('/number_template/<int:n>', strict_slashes=False)
def fun5(n):
    """shows html page when n is an int"""
    return render_template('5-number.html', n=n)


@res.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def fun6(n):
    """shows html page when n is an integer"""
    if n % 2 == 0:
        numEven = 'even'
    else:
        numEven = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           numEven=numEven)

if __name__ == '__main__':
    res.run(host='0.0.0.0', port='5000')
