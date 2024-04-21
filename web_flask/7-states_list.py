#!/usr/bin/python3
"""this intializes Flask web app
"""
from models import storage
from flask import Flask
from flask import render_template

res = Flask(__name__)


@res.route("/states_list", strict_slashes=False)
def fun():
    """this shows html page of state alphabetically.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@res.teardown_appcontext
def fun(xy):
    """this exits sql session"""
    storage.close()


if __name__ == "__main__":
    res.run(host="0.0.0.0")
