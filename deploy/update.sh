#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/coconut_api'

cd $PROJECT_BASE_PATH
git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart coconut_api

echo "DONE! :)"
