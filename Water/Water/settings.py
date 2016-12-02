"""
Django settings for Water project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os,sys
from os.path import join


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHARTIT_DIR = os.path.split(os.path.dirname(__file__))[0]
sys.path = [CHARTIT_DIR] + sys.path

PROJECT_ROOT=os.path.abspath(os.path.dirname(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#!#u0qwi-ni*xc$nyvox(-zlcp@&m5ac5#rj+ndda-%hrjjp+#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CHARTIT_JS_REL_PATH = '/chartit/js/'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'watres',
    'django_tables2',
    'xlwt',
    'crispy_forms',
    'django_filters',
    'djgeojson',
    'watstat',
    'chartit',
    'django_tables2_reports',
    'pyExcelerator',
  ]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_tables2_reports.middleware.TableReportMiddleware',
]

#'DIRS': [os.path.join(BASE_DIR, 'templates')],



EXCEL_SUPPORT = 'pyexcelerator'

ROOT_URLCONF = 'Water.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [

                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.debug',
                'django.contrib.messages.context_processors.messages',
                ],
        },
    },
]


WSGI_APPLICATION = 'Water.wsgi.application'

CRISPY_FAIL_SILENTLY = not DEBUG

CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default2': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'waternew',
        'USER': 'postgres',
        'PASSWORD': 'paxan',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },

    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'waternew',
        'USER': 'postgres',
        'PASSWORD': 'paxan',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },


}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATES_DIR=(
    join(PROJECT_ROOT,'templates'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = '/home/PycharmProjects/Water/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR,'static_root'))


LEAFLET_CONFIG = {

 'SPATIAL_EXTENT': (24.0, 51.00, 30, 55.00),
 'DEFAULT_CENTER': (27.0, 53.00),
 'NO_GLOBALS': False,
 'MIN_ZOOM': 5 ,
 'MAX_ZOOM': 25,
 'ATTRIBUTION_PREFIX': 'Powered by django-leaflet',
 'TILES': [ ('Sputnik','http://{s}.tiles.maps.sputnik.ru/tiles/kmt2/{z}/{x}/{y}.png',{}),
            ('OSM', 'http://tile.osm.org/{z}/{x}/{y}.png',{}),
            ('MapBox', 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {} ),
            ( 'Esri Areal', 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {}) ,
	         ]
}