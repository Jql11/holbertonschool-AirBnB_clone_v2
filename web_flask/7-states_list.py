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


@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template("7-states_list.html", dict=storage.all(State))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
