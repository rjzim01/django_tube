﻿# django_tube
git clone <repository_url>
cd <project_folder_name>
python -m venv env
env/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations <name of app>
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
