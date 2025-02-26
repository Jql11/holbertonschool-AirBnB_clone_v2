#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C " + str(text).replace('_', ' ')


@app.route("/python/", defaults={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return "Python " + str(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def show_post(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
