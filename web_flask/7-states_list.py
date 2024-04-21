#!/usr/bin/python3
"""this starts flask web app
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """this shows html page for states"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(xy):
    """this destroys session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
