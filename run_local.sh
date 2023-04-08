#!/usr/bin/env sh

python ./manage.py migrate
python ./manage.py collectstatic --noinput
python ./manage.py runserver 0.0.0.0:8080
