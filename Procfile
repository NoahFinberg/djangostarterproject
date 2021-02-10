release: python manage.py migrate

web: gunicorn djauth.wsgi --log-file -

worker: python manage.py rqworker default