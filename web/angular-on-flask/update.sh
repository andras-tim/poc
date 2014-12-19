#!/bin/bash -e

cd "$(dirname $0)"

cd orig_angular-phonecat
git checkout -f "step-$1"
cd ..

find app/static -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} \;
find orig_angular-phonecat/app -mindepth 1 -maxdepth 1 -exec cp -r {} app/static/ \;
