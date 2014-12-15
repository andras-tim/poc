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
