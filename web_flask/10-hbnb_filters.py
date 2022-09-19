#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""

from flask import Flask
from flask import render_template
from models import storage
from models import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    return render_template("10-hbnb_filters.html",
                           dict=storage.all(State),
                           amenity_dict=storage.all(Amenity))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
