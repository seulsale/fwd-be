release: python manage.py migrate --noinput
web: gunicorn fwd_be.wsgi --log-file -