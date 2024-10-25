import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for the project
SECRET_KEY = 'django-insecure-e0s#hyx5a(x^0h=e_^7h=wxtmkl1m-0epselz#d5^^lqkp$9f+'

# DEBUG mode should be disabled in production
DEBUG = bool(int(os.environ.get('DEBUG', 1)))

# Hosts allowed to connect to the application
ALLOWED_HOSTS = [
                 'ec2-52-65-140-222.ap-southeast-2.compute.amazonaws.com',
                 '127.0.0.1:8000'
                 ]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'ccapi',
    'storages',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}



# Assuming BASE_DIR is defined
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # Ensure this is set

# Static root (used only during deployment/production)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_root')  # Different directory for production

# Static files directories (used only during development)
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),  # Your development static files
    ]
else:
    STATICFILES_DIRS = []  # Ensure this is empty for production

# Ensure STATICFILES_DIRS and STATIC_ROOT are not the same directory
if DEBUG and STATICFILES_DIRS:
    assert os.path.abspath(STATICFILES_DIRS[0]) != os.path.abspath(STATIC_ROOT), (
        "STATICFILES_DIRS and STATIC_ROOT should not be the same directory."
    )

# Media files settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default coconut rates (custom setting)
DEFAULT_COCONUT_RATE = [0.85]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
