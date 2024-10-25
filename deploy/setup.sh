#!/usr/bin/env bash

set -e

# Set to URL of your git repo
PROJECT_GIT_URL='https://github.com/sanjithhithub/coconut_api.git'

# Path where the project will be deployed
PROJECT_BASE_PATH='/usr/local/apps/coconut_api'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite3, and pip
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite3 python3-pip supervisor nginx git

# Create project directory and clone the GitHub repo
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Set up Python virtual environment
python3 -m venv $PROJECT_BASE_PATH/env

# Install required Python packages inside the virtual environment
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt uwsgi==2.0.21

# Run Django migrations
$PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py migrate

# Setup Supervisor to run the uwsgi process for your project
cp $PROJECT_BASE_PATH/deploy/supervisor_coconut_api.conf /etc/supervisor/conf.d/coconut_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart coconut_api

# Setup Nginx to make your application accessible
cp $PROJECT_BASE_PATH/deploy/nginx_coconut_api.conf /etc/nginx/sites-available/coconut_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/coconut_api.conf /etc/nginx/sites-enabled/coconut_api.conf
systemctl restart nginx.service

echo "Deployment of coconut API completed!"
