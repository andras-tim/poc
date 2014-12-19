#!/bin/bash

# Update system
sudo apt-get install build-essential python3 python-virtualenv

# Prepare virtual environment
if [ ! -e flask ]; then
    virtualenv -p /usr/bin/python3.4 flask
fi
flask/bin/pip install pip --upgrade
flask/bin/pip install setuptools --upgrade

flask/bin/pip install -r requirements.txt --upgrade

flask/bin/pip install git+git://github.com/mitsuhiko/babel.git --global-option import_cldr
flask/bin/pip install flask-babel --upgrade
#flask/bin/pip install guess_language
flask/bin/pip install https://bitbucket.org/spirit/guess_language/downloads/guess_language-spirit-0.5a4.tar.bz2
