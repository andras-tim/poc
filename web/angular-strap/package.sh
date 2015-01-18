#!/bin/bash -e

function do_install()
{
    server/package.sh preinstall
    client/package.sh preinstall

    server/package.sh postinstall
    client/package.sh postinstall
}

function do_start()
{
    server/package.sh start
}

function do_clear()
{
    server/package.sh clear
    client/package.sh clear
}


cd "$(dirname "$0")"
source .main.sh
