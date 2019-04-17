#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations weirdapp
python manage.py migrate weirdapp
python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput
