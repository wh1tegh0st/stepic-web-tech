#!/bin/bash

sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# Newer than the system gunicorn
cd web || exit 1
source .venv/bin/activate
gunicorn -c etc/gunicorn.hello.config.py hello:app &
cd ask || exit 1
gunicorn -c ../etc/gunicorn.ask.config.py ask.wsgi &