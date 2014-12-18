from flask import Flask

app = Flask(__name__)


# Init models and views (must be the last)
from app import data, api
