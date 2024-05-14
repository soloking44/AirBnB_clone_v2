#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


<<<<<<< HEAD
@app.route('/airbnb-onepage/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
@app.route("/airbnb-onepage", strict_slashes=False)
def index():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
>>>>>>> origin/app-server
