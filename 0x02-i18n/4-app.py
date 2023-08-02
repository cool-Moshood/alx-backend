#!/usr/bin/env python3
"""a flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """confi class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Check if the lang parameter is specified in the query string"""
    user_lang = request.args['locale']
    if user_lang in ['en', 'fr']:
        return user_lang

    """If lang parameter is not specified, use Accept-Language header"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index():
    """Route function"""
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run(port=5000)
