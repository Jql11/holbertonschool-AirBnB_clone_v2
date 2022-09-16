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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    return render_template("8-cities_by_states.html", dict=storage.all(State))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
