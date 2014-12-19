from flask import Flask


app = Flask(__name__, static_url_path='/app')


# Init models and views (must be the last)
from app import data, api, views
