from pathlib import Path
import os

# environment vars
import environ
env = environ.Env()
environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# can find the endpoint's secret by running `stripe listen` in CLI
STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET")

# stripe data
STRIPE_PK = env("STRIPEPK")
STRIPE_SK = env("STRIPESK")
STRIPE_DOMAIN = env("STRIPE_DOMAIN")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# rest framework global settings
# authentication classes: https://www.django-rest-framework.org/api-guide/settings/#default_authentication_classes
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # permission policy: https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy
    # can override these in views. Don't forget to add a comma
    'DEFAULT_PERMISSION_CLASSES': (
        # allow anyone to access api data
        # 'rest_framework.permissions.AllowAny', 
        # do not allow anyone to access API endpoints unless user is authenticated
        # 'rest_framework.permissions.IsAuthenticated', 
        # allow full access to authenticated users, but allow read-only access to unauthenticated users
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer', # makes api views JSON data only
    ),
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # add drf dependencies
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    # djoser is a REST implementation of Django authentication system. Provides token based authentication
    'djoser',
    # add apps
    'flps_app',
    'tracks_app',
    # custom user app
    'lctec_user',
    # order app
    'order_app',
]

# frontend server. Change to live server address for production
ADDRESS = env('ALLOWED_ORIGINS')
CORS_ALLOWED_ORIGINS = [
    ADDRESS, 
]

# set my custom user model (appname.Django model name)
AUTH_USER_MODEL = 'lctec_user.Lctec_User'


# add custom backend, if it fails, Django will use default backend
# also may be needed for admin page
#  to set custom backend, use this syntax:
# appname.backendfile.pyname.modelname
AUTHENTICATION_BACKENDS = (
    'sheriff_crandy_project.lctec_backend.Lctec_Backend',
    # 'django.contrib.auth.backends.ModelBackend',
    )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # this has to go above CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sheriff_crandy_project.urls'

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

WSGI_APPLICATION = 'sheriff_crandy_project.wsgi.application'


# PostgreSQL config
DATABASES = {
    'default': {
        # postgresql
        'ENGINE': env('DBENGINE'),
        # name of database
        'NAME': env('DBNAME'),
        # owner of database
        'USER': env('DBUSER'),
        'PASSWORD': env('DBPASSWORD'),
        # specify which machine where db is installed
        # connect through TCP sockets, 
        'HOST': env('DBHOST')
    }

}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
'''
AUTH_PASSWORD_VALIDATORS = [

    
    {
        # checks if the user name/password is similiar to password
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # minimum length of a password. Don't really need this for my website
        # warn user in frontend to change password but don't force it
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        # checks against commonly used passwords
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
        # prevents password from being entirely numeric
    {   
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
'''


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'

# absolute path where collectstatic will collect static files for deployment
# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


# media dir for images and audio files. This dir is created when the first model objects are created (either through admin page or otherwise)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
