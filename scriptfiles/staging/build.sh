#!/bin/sh
# exit on error
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000
exec "$@"
