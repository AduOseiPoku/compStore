#!/bin/sh
set -e

echo "--> Collecting static files..."
python manage.py collectstatic --noinput

echo "--> Applying database migrations..."
python manage.py migrate --noinput

echo "--> Seeding/verifying catalog services and products..."
python manage.py seed_catalog || true
python manage.py seed_100_products || true

echo "--> Starting Gunicorn web server on port ${PORT:-8000}..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
