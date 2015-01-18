#!/bin/bash -e
PYTHON_VERSION=3.4


function do_preinstall()
{
    packages="build-essential python${PYTHON_VERSION} python${PYTHON_VERSION}-dev libyaml-dev" #libpython${PYTHON_VERSION}-dev
    if [ "${GLOBAL_INSTALL}" == true ]
    then
        packages="${packages} python3-pip"
    else
        packages="${packages} python-virtualenv"
    fi
    sudo apt-get install ${packages}
}

function do_postinstall()
{
    pip="sudo pip3"
    if [ "${GLOBAL_INSTALL}" == false ]
    then
        pip='flask/bin/pip'

        # Install virtualenv
        if [ ! -e flask ]
        then
            virtualenv -p /usr/bin/python${PYTHON_VERSION} flask
        fi
    fi

    # Update Python packages
    ${pip} install --upgrade pip setuptools
    ${pip} install -r requirements.txt --upgrade

    # Create directories
    if [ ! -e tmp ]
    then
        mkdir -p tmp
    fi

    if [ "${PRODUCTION}" == false ]
    then
        # Create symlinks
        if [ ! -e app/static ]
        then
            ln -s ../../client/app app/static
        fi
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
    python="python${PYTHON_VERSION}"
    if [ "${GLOBAL_INSTALL}" == false ]
    then
        python='flask/bin/python'
    fi
    ${python} run.py
}


cd "$(dirname "$0")"
source ../.main.sh
