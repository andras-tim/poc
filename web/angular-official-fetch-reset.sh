#!/bin/bash -e
DIR='angular-official'

if [ ! -e "${DIR}/.git" ]
then
    git clone --depth=14 https://github.com/angular/angular-phonecat.git "${DIR}"
fi

cd "${DIR}"
git checkout -f step-11

exit 0
