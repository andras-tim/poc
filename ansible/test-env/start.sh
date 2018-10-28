#!/bin/bash
set -eufo pipefail
BASE_DIR="$(cd "$(dirname "$0")"; pwd)"
ROOT_DIR="$(cd "${BASE_DIR}/.."; pwd)"
IMAGE_NAME='ansible-test-image'
CONTAINER_NAME='ansible-test'

set -x
docker build -t "${IMAGE_NAME}" "${BASE_DIR}"

docker rm "${CONTAINER_NAME}" &>/dev/null || true

docker run -ti \
    --cap-add SYS_ADMIN \
    -v '/var/run/docker.sock:/var/run/docker.sock' \
    -v "${ROOT_DIR}:/aaa" \
    --name "${CONTAINER_NAME}" \
    "$@" \
    "${IMAGE_NAME}"
