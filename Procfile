release: python manage.py migrate

web: gunicorn djangostarterproject.wsgi --log-file -

worker: python manage.py rqworker default