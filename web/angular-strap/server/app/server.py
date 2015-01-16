from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

from .config import Config
from . res.restfulApi import RestfulApiWithoutSimpleAuth


config = Config.read()

app = Flask(__name__, static_url_path='/%s' % config.App.NAME)
app.config.update(config["Flask"])
# import pprint; app.logger.debug("Flask config:\n%s" % pprint.pformat(app.config))

# flask-sqlalchemy
db = SQLAlchemy(app)

# flask-login
lm = LoginManager()
lm.init_app(app)

# flask-restful
api = RestfulApiWithoutSimpleAuth(app)


# flask-bcrypt
bcrypt = Bcrypt(app)


# Init models and views (must be the last)
from app import views
