#!/bin/bash -e

function do_preinstall()
{
    if [ ! -e '/etc/apt/sources.list.d/nodesource.list' ]
    then
        wget -q 'https://deb.nodesource.com/setup' -O - | sudo bash -
    fi
    sudo apt-get install nodejs
}

function do_postinstall()
{
    npm install
    node_modules/bower/bin/bower install
    npm run update-webdriver
}

function do_clear()
{
    if [ -e app/bower_components ]
    then
        rm -rf app/bower_components
    fi
}

function do_test()
{
    npm test
}

function do_test_single_run()
{
    npm run test-single-run
}

function do_update_webdriver()
{
    npm run update-webdriver
}

function do_protractor()
{
    npm run protractor
}


cd "$(dirname "$0")"
source ../.main.sh
