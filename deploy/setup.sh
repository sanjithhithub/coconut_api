#!/usr/bin/env bash

set -e

# Set to URL of your git repo.
PROJECT_GIT_URL='https://github.com/sanjithhithub/coconut_api.git'

# Path where your project will be deployed.
PROJECT_BASE_PATH='/usr/local/apps/coconut_api/api/'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite, pip, and other dependencies
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv python3-pip sqlite3 supervisor nginx git build-essential libpcre3-dev libssl-dev

# Create project directory and clone your GitHub repo
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Setup Python virtual environment
python3 -m venv $PROJECT_BASE_PATH/env

# Install required Python packages inside the virtual environment
$PROJECT_BASE_PATH/env/bin/pip install --upgrade pip  # Upgrade pip
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi  # Install uwsgi without a specific version

# Run Django migrations
$PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py migrate

# Setup Supervisor to run the uwsgi process for your project
cp $PROJECT_BASE_PATH/deploy/supervisor_coconut_api.conf /etc/supervisor/conf.d/coconut_api.conf

supervisorctl reread
supervisorctl update
supervisorctl restart coconut_api

# Setup Nginx to make your application accessible
cp $PROJECT_BASE_PATH/deploy/nginx_coconut_api.conf /etc/nginx/sites-available/coconut_api.conf

# Check if the symbolic link already exists and remove it if necessary
if [ -L /etc/nginx/sites-enabled/coconut_api.conf ]; then
    rm /etc/nginx/sites-enabled/coconut_api.conf
fi

# Create a new symbolic link for the Nginx configuration
ln -s /etc/nginx/sites-available/coconut_api.conf /etc/nginx/sites-enabled/coconut_api.conf

# Restart Nginx to apply changes
systemctl restart nginx.service

echo "Deployment of coconut API completed"
