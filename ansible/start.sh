#!/bin/bash
set -eufo pipefail

cd "$(dirname "$0")"
export ANSIBLE_NOCOWS=1

set -x
ansible-playbook -i 'hosts' 'test.yml' "$@"
