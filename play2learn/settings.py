"""
Django settings for play2learn project.
Generated by 'django-admin startproject' using Django 4.2.
For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-g7e4)cdx(!g2eg&!)_e@xwd0#0t@#0ne*b_jh^1x+9#y4jl9uf"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    # Third-party
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # local apps
    "common.apps.CommonConfig",
    "contact.apps.ContactConfig",
    "games.apps.GamesConfig",
    "pages.apps.PagesConfig",
    "reviews.apps.ReviewsConfig",
    "users.apps.UsersConfig",
]

SITE_ID = 1
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  
    'allauth.account.middleware.AccountMiddleware',  
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = "play2learn.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "play2learn.wsgi.application"
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "play2learn",
        "USER": "postgres",
        "PASSWORD": "Joey0731",
        "HOST": "localhost",
        "PORT": 5432
    }
}
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, even w/o `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth`-specific auth methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
# AUTHENTICATION SETTINGS
AUTH_USER_MODEL = "users.CustomUser"
LOGIN_URL = "account_login"
LOGIN_REDIRECT_URL = "pages:homepage"
## django-allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'email' # Default: 'username'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1 # Default: 3
ACCOUNT_EMAIL_REQUIRED = True # Default: False
ACCOUNT_EMAIL_VERIFICATION = 'none' # Changed to `none` because no sendgrid account
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5 # Default: 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300 # Default 300
ACCOUNT_LOGOUT_REDIRECT_URL ='account_login' # Default: '
ACCOUNT_USERNAME_REQUIRED = False # Default: True
ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email settings for SendGrid
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

# Optional settings for SendGrid
SENDGRID_SANDBOX_MODE_IN_DEBUG = False  # Set to True to avoid sending emails in DEBUG mode
SENDGRID_ECHO_TO_STDOUT = True  # Set to True to output emails to the console (for debugging)

DEFAULT_FROM_EMAIL = 'woodcoty99@gmail.com'  # The default "from" email address
ADMIN_EMAIL = 'woodcoty99@gmail.com'

# Conditional import of local settings
if os.environ.get('ENVIRONMENT') != 'production':
    from .local_settings import *
# DON'T PUT ANYTHING BELOW THIS
