#!/bin/bash -e

# Update system
sudo apt-get install build-essential python3 python-virtualenv


# Prepare virtual environment
virtualenv -p /usr/bin/python3 flask
flask/bin/pip install flask
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install sqlalchemy-migrate
flask/bin/pip install flask-whooshalchemy
flask/bin/pip install flask-wtf
flask/bin/pip install flask-babel
flask/bin/pip install guess_language
flask/bin/pip install flipflop
flask/bin/pip install coverage


# Prepare file system of virtual environment
mkdir -p {app/{static,templates},tmp}


exit 0
