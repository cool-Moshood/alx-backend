#!/usr/bin/env python3
"""a flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
Babel = Babel(app)


def get_locale():
    """determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """Route function"""
    return render_template("2-index.html")


app.config.from_object(Config)


if __name__ == '__main__':
    app.run(port=5000)
