#!/bin/bash
pip install -r backend/requirements.txt
python backend/manage.py migrate
python backend/manage.py makemigrations listofusers
python backend/manage.py runserver