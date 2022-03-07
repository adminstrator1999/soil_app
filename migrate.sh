#!/bin/bash
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-'admin@gmail.com'}
SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-'superseckretpassword'}
/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true