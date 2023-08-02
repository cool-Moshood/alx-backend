#!/usr/bin/env python3
"""a flask app"""
import babel
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
Babel = Babel(app)


@app.route("/")
def index():
    """Route function"""
    lang = request.args.get("lang", "en")
    babel.locale_selector_func = lambda: lang

    return render_template("1-index.html")


app.config.from_object(Config)


if __name__ == '__main__':
    app.run(port=5000)
