# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


# https://pythonhosted.org/Flask-SQLAlchemy/config.html
# http://docs.sqlalchemy.org/en/rel_0_9/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqldb
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://user:pass@localhost/poc-microblog'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-debugging-testing-and-profiling
#SQLALCHEMY_RECORD_QUERIES = True


# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None


# administrator list
ADMINS = ['andras.tim@gmail.com']


# pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50


# available languages
LANGUAGES = {
    'en': 'English',
    'hu': 'Magyar'
}


# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = 'foo_microblog'  # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = 'fOoMicRobloGMstranSlaTorClient1sgavI07D+cYE='  # enter your MS translator app secret here
