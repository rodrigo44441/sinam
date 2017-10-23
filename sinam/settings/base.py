#import os

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p+v%c#=c@0sux%^=ayv5^agpltt8ob^an=c4ity9f7#*lifj1n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rodrigo44441@gmail.com'
EMAIL_HOST_PASSWORD = 'bolsoputo21761'
EMAIL_USE_TLS = True

'''
Para usar gmail hay que desbloquear gmail
https://accounts.google.com/displayunlockcaptcha
'''

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.tienda',
    'apps.empresa',
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

ROOT_URLCONF = 'sinam.urls'

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
                'apps.tienda.porcessors.processorsdatos',
                'apps.tienda.porcessors.processorsfaq',
                'apps.tienda.porcessors.processorsredes',
                'apps.tienda.porcessors.processorsnosotros',
            ],
        },
    },
]

GRAPPELLI_ADMIN_TITLE = 'SINAM'

WSGI_APPLICATION = 'sinam.wsgi.application'



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

#TEMPLATE_CONTEXT_PROCESSORS = TCP + (
 #       'apps.empresa.processors.miprocessors',
  #  )