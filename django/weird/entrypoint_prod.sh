#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations weirdapp
python manage.py migrate weirdapp
python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput

user_id=$(stat -c '%u:%g' /django)
chown -R ${user_id} /django

python manage.py runserver 0.0.0.0:80
