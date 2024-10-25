#!/usr/bin/env bash

set -e  # Exit immediately if a command exits with a non-zero status

# Set to URL of your git repo.
PROJECT_GIT_URL='https://github.com/sanjithhithub/coconut_api.git'

# Path where your project will be deployed.
PROJECT_BASE_PATH='/usr/local/apps/coconut_api/api/'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install dependencies
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv python3-pip sqlite3 supervisor nginx git build-essential libpcre3-dev libssl-dev

# Create project directory and clone your GitHub repo
mkdir -p $PROJECT_BASE_PATH
if [ ! -d "$PROJECT_BASE_PATH/.git" ]; then
    git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH
else
    echo "Project already cloned, pulling latest changes..."
    cd $PROJECT_BASE_PATH
    git pull
fi

# Setup Python virtual environment
python3 -m venv $PROJECT_BASE_PATH/env

# Install required Python packages inside the virtual environment
$PROJECT_BASE_PATH/env/bin/pip install --upgrade pip  # Upgrade pip
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi  # Install uwsgi without a specific version

# Run Django migrations
$PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py migrate

# Collect static files
$PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py collectstatic --noinput

# Setup Supervisor
cp $PROJECT_BASE_PATH/deploy/supervisor_coconut_api.conf /etc/supervisor/conf.d/coconut_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart coconut_api

# Setup Nginx
cp $PROJECT_BASE_PATH/deploy/nginx_coconut_api.conf /etc/nginx/sites-available/coconut_api.conf

# Create symbolic link for Nginx configuration
if [ -L /etc/nginx/sites-enabled/coconut_api.conf ]; then
    rm /etc/nginx/sites-enabled/coconut_api.conf
fi
ln -s /etc/nginx/sites-available/coconut_api.conf /etc/nginx/sites-enabled/coconut_api.conf

# Restart Nginx
systemctl restart nginx.service

echo "Deployment of coconut API completed."
