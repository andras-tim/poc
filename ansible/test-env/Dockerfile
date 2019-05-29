FROM ubuntu:bionic

RUN set -xe \
    && apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common

RUN set -xe \
    && apt-get install -y \
        ssh \
        sudo \
    && mkdir /run/sshd \
    \
    && mkdir -p "${HOME}/.ssh" \
    && ssh-keygen -qf "${HOME}/.ssh/id_rsa" -t rsa -N '' \
    && cp "${HOME}/.ssh/id_rsa.pub" "${HOME}/.ssh/authorized_keys" \
    \
    && /usr/sbin/sshd \
    && ssh-keyscan -H localhost > "${HOME}/.ssh/known_hosts" \
    && pkill sshd

RUN set -xe \
    && apt-add-repository -y ppa:ansible/ansible \
    && apt-get install -y \
        ansible

ENTRYPOINT ["/aaa/test-env/entrypoint.sh"]
CMD ["/bin/bash"]
