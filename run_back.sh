#!/bin/bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations listofusers
python manage.py migrate
python manage.py loaddata roles.json
python manage.py loaddata users.json
python manage.py runserver