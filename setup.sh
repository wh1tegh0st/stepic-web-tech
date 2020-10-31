#!/bin/bash

# The environment is too old, update it
sudo apt-get update
sudo apt-get install -y python3.5
sudo apt-get install -y python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install --upgrade pip

DEBIAN_FRONTEND=noninteractive sudo -E apt-get install -y -q mysql-server-5.6  # no prompt

virtualenv -p python3 web/.venv
. web/.venv/bin/activate

pip install --upgrade gunicorn
pip install --upgrade django==2.1
pip install --upgrade mysqlclient

deactivate