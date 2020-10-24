#!/bin/bash

# The environment is too old, update it
sudo apt-get update
sudo apt-get install -y python3.5
sudo apt-get install -y python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install --upgrade pip

virtualenv -p python3 web/.venv
. .venv/bin/activate

pip install --upgrade gunicorn

deactivate