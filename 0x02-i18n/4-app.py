#!/usr/bin/env python3
"""a flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)
Babel = Babel(app)


class Config:
    """confi class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """Check if the lang parameter is specified in the query string"""
    user_lang = request.args.get("locale")
    if user_lang and user_lang.lower() in app.config["LANGUAGES"]:
        print(user_lang)
        return user_lang.lower()

    """If lang parameter is not specified, use Accept-Language header"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/")
def index():
    """Route function"""
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run(port=5000)
