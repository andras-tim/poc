from flask import Flask
from flask.ext.babel import Babel

app = Flask(__name__)


# Init Flask plugins - Multi language
babel = Babel(app)


# Init models and views (must be the last)
from app import data, api, views
