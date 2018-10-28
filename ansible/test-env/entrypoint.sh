#!/bin/bash
set -xeufo pipefail

#mkdir /run/sshd
/usr/sbin/sshd

cd /aaa
exec "$@"
