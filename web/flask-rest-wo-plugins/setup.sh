#!/bin/bash

# Update system
sudo apt-get install build-essential python3 python-virtualenv

# Prepare virtual environment
if [ ! -e flask ]; then
    virtualenv -p /usr/bin/python3.4 flask
fi
flask/bin/pip install pip --upgrade
flask/bin/pip install setuptools --upgrade
flask/bin/pip install flask
flask/bin/pip install flask-httpauth
