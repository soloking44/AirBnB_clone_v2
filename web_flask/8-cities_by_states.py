#!/usr/bin/python3
"""
this is flask intialize
"""

from flask import Flask, render_template
from models import *
from models import storage
res = Flask(__name__)


@res.route('/cities_by_states', strict_slashes=False)
def fun():
    """list state accordingly"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)

@res.teardown_appcontext
def fun2(exception):
    """exit storage"""
    storage.close()

if __name__ == '__main__':
    res.run(host='0.0.0.0', port='5000')
