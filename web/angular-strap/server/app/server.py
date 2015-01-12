from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.bcrypt import Bcrypt

from .config import Config


config = Config.read()

app = Flask(__name__, static_url_path='/%s' % config.App.NAME)
app.config.update(config["Flask"])
# import pprint; app.logger.debug("Flask config:\n%s" % pprint.pformat(app.config))

# flask-sqlalchemy
db = SQLAlchemy(app)

# flask-restful
api = restful.Api(app)

# flask-bcrypt
bcrypt = Bcrypt(app)

# flask-httpauth
auth = HTTPBasicAuth()


# Init models and views (must be the last)
from app import views
