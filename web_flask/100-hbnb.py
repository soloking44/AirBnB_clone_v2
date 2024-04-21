#!/usr/bin/python3
"""this starts flask web app at port 5000
"""
from models import storage
from flask import Flask
from flask import render_template

res = Flask(__name__)


@res.route("/hbnb", strict_slashes=False)
def fun():
    """shows HBNB pages in html"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@res.teardown_appcontext
def fun2(xy):
    """destroys session."""
    storage.close()


if __name__ == "__main__":
    res.run(host="0.0.0.0")
