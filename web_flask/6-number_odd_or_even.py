#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""

from flask import Flask
from flask import render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if (n % 2) == 0:
        text = "even"
    else:
        text = "odd"
    return render_template("6-number_odd_or_even.html", n=n, text=text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
