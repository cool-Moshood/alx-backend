#!/usr/bin/env python3
"""a flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)
Babel = Babel(app)


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """Check if the lang parameter is specified in the query string"""
    user_lang = request.args.get("lang")
    if user_lang in app.config["LANGUAGES"]:
        return user_lang

    """If lang parameter is not specified, use Accept-Language header"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route("/")
def index():
    """Route function"""
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(port=5000)
