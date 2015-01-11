import os
from flask import Flask

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(__name__, static_url_path='/test')


# Init models and views (must be the last)
from app import data, api, views
