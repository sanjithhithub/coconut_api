#!/usr/bin/env bash

set -e  # Exit on any error

# Set the URL of your GitHub repository
PROJECT_GIT_URL='https://github.com/sanjithhithub/coconut_api.git'

# Set the path where the project will be deployed
PROJECT_BASE_PATH='/usr/local/apps/coconut_api'

# Set the locale
echo "Setting locale..."
locale-gen en_GB.UTF-8

# Update package list and install dependencies
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite3 python3-pip supervisor nginx git

# Create the project directory if it doesn't exist
mkdir -p $PROJECT_BASE_PATH

# Clone the project from GitHub (overwrite if it exists)
if [ -d "$PROJECT_BASE_PATH/.git" ]; then
    echo "Repository already exists, pulling the latest changes..."
    cd $PROJECT_BASE_PATH
    git pull
else
    echo "Cloning repository..."
    git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH
fi

# Set up Python virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv $PROJECT_BASE_PATH/env

# Install the required Python packages inside the virtual environment
echo "Installing Python packages..."
$PROJECT_BASE_PATH/env/bin/pip install --upgrade pip  # Upgrade pip
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt uwsgi==2.0.21

# Run Django migrations
echo "Running Django migrations..."
$PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py migrate

# Collect static files (if needed)
echo "Collecting static files..."
$PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py collectstatic --noinput

# Configure Supervisor to manage uWSGI for the project
echo "Configuring Supervisor..."
cp $PROJECT_BASE_PATH/deploy/supervisor_coconut_api.conf /etc/supervisor/conf.d/coconut_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart coconut_api

# Configure Nginx to serve the application
echo "Configuring Nginx..."
cp $PROJECT_BASE_PATH/deploy/nginx_coconut_api.conf /etc/nginx/sites-available/coconut_api.conf
rm -f /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/coconut_api.conf /etc/nginx/sites-enabled/coconut_api.conf
systemctl restart nginx.service

echo "Deployment of coconut API completed successfully!"
