import os
from pathlib import Path
import dj_database_url

# 1. Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. SECURITY: Load Secret Key from Heroku Config Vars (Req #10)
SECRET_KEY = os.environ.get('SECRET_KEY',
                            'django-insecure-local-development-key')

# 3. SECURITY: Debug should be False on Heroku
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['ez-book.herokuapp.com', '127.0.0.1', 'localhost',
                 '.herokuapp.com']

# 4. Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',  # Your new app name for EZ Book
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 5. URLs and Templates
ROOT_URLCONF = 'book.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'book.wsgi.application'


DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        ssl_require=False if DEBUG else True
    )
}

# 7. Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.User'
     'AttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.'
     'MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.'
     'CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.'
     'NumericPasswordValidator', },
]

# 8. Internationalization
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 9. Static Files (CSS/JS) (Req #4 & #5)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 10. Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 11. Authentication Redirects
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
