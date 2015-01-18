#!/bin/bash -e
PYTHON_VERSION=3.4


function do_preinstall()
{
    sudo apt-get install build-essential python${PYTHON_VERSION} python${PYTHON_VERSION}-dev python-virtualenv libyaml-dev #libpython${PYTHON_VERSION}-dev
}

function do_postinstall()
{
    # Install virtualenv
    if [ ! -e flask ]
    then
        virtualenv -p /usr/bin/python${PYTHON_VERSION} flask
    fi

    # Update Python packages
    flask/bin/pip install --upgrade pip setuptools
    flask/bin/pip install -r requirements.txt --upgrade --allow-external mysql-connector-python

    # Create directories
    if [ ! -e tmp ]
    then
        mkdir -p tmp
    fi

    # Create symlinks
    if [ ! -e app/static ]
    then
        ln -s ../../client/app app/static
    fi
}

function do_clear()
{
    # Remove symlinks
    if [ -e app/static ]
    then
        rm app/static
    fi

    # Remove directories
    if [ -e tmp ]
    then
        rm -r tmp
    fi

    # Remove virtualenv
    if [ -e flask ]
    then
        rm -r flask
    fi
}

function do_start()
{
    flask/bin/python${PYTHON_VERSION} run.py
}


cd "$(dirname "$0")"
source ../.main.sh
