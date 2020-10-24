#!/bin/bash

sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# Newer than the system gunicorn
cd web || exit 1
. .venv/bin/activate
gunicorn -c etc/gunicorn.config.py hello:app &