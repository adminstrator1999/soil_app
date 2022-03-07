SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-'admin@gmail.com'}
cd /soil_app
source venv/bin/activate
python manage.py migrate --noinput
python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true