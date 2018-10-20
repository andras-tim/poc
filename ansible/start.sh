#!/bin/bash
set -eufo pipefail

cd "$(dirname "$0")"
export ANSIBLE_NOCOWS=1

ansible-playbook -i 'hosts' 'test.yml'
