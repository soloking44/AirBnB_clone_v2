#!/usr/bin/python3
"""this starts flask web app at port 5000
"""
from models import storage
from flask import Flask
from flask import render_template

res = Flask(__name__)


@res.route("/hbnb_filters", strict_slashes=False)
def fun():
    """shows HBNB pages in html"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@res.teardown_appcontext
def fun2(xy):
    """destroys session."""
    storage.close()


if __name__ == "__main__":
    res.run(host="0.0.0.0")
