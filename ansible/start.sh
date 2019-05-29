#!/bin/bash
set -eufo pipefail

cd "$(dirname "$0")"
export ANSIBLE_NOCOWS=1

set -x

ansible-galaxy install -r 'requirements.yml'
ansible-playbook -i 'hosts' 'test.yml' "$@"
