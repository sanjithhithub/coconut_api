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
cat <<EOL > /etc/supervisor/conf.d/coconut_api.conf
[program:coconut_api]
command=$PROJECT_BASE_PATH/env/bin/uwsgi --ini $PROJECT_BASE_PATH/uwsgi.ini
directory=$PROJECT_BASE_PATH
user=www-data
autostart=true
autorestart=true
redirect_stderr=true
EOL

supervisorctl reread
supervisorctl update
supervisorctl restart coconut_api

# Setup Nginx to make your application accessible
cat <<EOL > /etc/nginx/sites-available/coconut_api.conf
upstream django {
    server 127.0.0.1:8000;  # Ensure your app is listening on this port
}

server {
    listen 80;  # Listen on port 80 for HTTP requests
    server_name your_domain_or_ip;  # Change this to your server's domain or IP

    # Serve static files
    location /static {
        alias /usr/local/apps/coconut_api/api/static;  # Adjust path to your static files
    }

    # Serve media files (optional)
    location /media {
        alias /usr/local/apps/coconut_api/api/media;  # Adjust path to your media files
    }

    location / {
        proxy_pass http://django;  # Forward requests to the Django app
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_redirect off;
    }

    # Optional: Handle 404 errors for missing static files
    error_page 404 /404.html;
    location = /404.html {
        root /usr/local/apps/coconut_api/api/static;  # Change path if needed
    }
}
EOL

# Check if the symbolic link already exists and remove it if necessary
if [ -L /etc/nginx/sites-enabled/coconut_api.conf ]; then
    rm /etc/nginx/sites-enabled/coconut_api.conf
fi

# Create a new symbolic link for the Nginx configuration
ln -s /etc/nginx/sites-available/coconut_api.conf /etc/nginx/sites-enabled/coconut_api.conf

# Restart Nginx to apply changes
systemctl restart nginx.service

echo "Deployment of coconut API completed"
