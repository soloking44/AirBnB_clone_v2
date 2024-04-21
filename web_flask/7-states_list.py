#!/usr/bin/python3
"""
this initialize web flask
"""

from flask import Flask, render_template
from models import *
from models import storage
res = Flask(__name__)


@res.route('/states_list', strict_slashes=False)
def fun():
    """this outputs states in html accordingly"""
    states = sorted(list(storage.all("State").values()), key=lambda mn: mn.name)
    return render_template('7-states_list.html', states=states)


@res.teardown_appcontext
def fun2(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    res.run(host='0.0.0.0', port='5000')
