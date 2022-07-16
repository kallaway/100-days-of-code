#!/bin/bash

pushd utils/twitter || exit 1

source . ./venv/bin/activate
python3 main.py

popd || exit 1