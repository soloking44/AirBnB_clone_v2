#!/usr/bin/python3
"""this starts flask app at port 5000
"""
from models import storage
from flask import Flask
from flask import render_template

res = Flask(__name__)

@res.teardown_appcontext
def fun(self):
    """ this function closes session """
    storage.close()


@res.route('/states', strict_slashes=False)

@res.route("/states/<id>", strict_slashes=False)
def fun2(id):
    """this functions showa HTML page with id information."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@res.teardown_appcontext
def fun3(exc):
    """this closes session."""
    storage.close()


if __name__ == "__main__":
    res.run(host="0.0.0.0")
