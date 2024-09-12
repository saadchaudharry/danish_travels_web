#!/bin/sh

# Run makemigrations
python manage.py makemigrations

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the application
exec gunicorn --workers=1 --bind=0.0.0.0:8000 hrasc.wsgi:application
