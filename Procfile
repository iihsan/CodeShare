release: python manage.py migrate && python manage.py collectstatic --no-input
web: gunicorn --bind :8000 --workers 3 --threads 2 CodeShare.wsgi:application