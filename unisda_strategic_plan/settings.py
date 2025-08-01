"""
Django settings for unisda_strategic_plan project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path
from django.urls import reverse_lazy
from dotenv import load_dotenv

LOGIN_URL = reverse_lazy("login")  # Redirect to login if unauthenticated
LOGOUT_REDIRECT_URL = '/'

# Optional: Customize 403 error handler for insufficient permissions
HANDLER403 = "strategic_planning.views.permission_denied"
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR/".eVar", ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-(asfcb0lz0#^w=19m45r(_7a@x-v^9oturg&g0zzu#piii-o08')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'strategic_planning',
]
AUTH_USER_MODEL = 'strategic_planning.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add WhiteNoise right after security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Add this for better static file serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'unisda_strategic_plan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # ref our templates folder
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'strategic_planning.context_processors.strategic_themes',
                'strategic_planning.context_processors.strategic_objectives_context',       
            ],
        },
    },
]

JAZZMIN_SETTINGS = {
    "site_title": "My Dashboard",
    "site_header": "Planning Dashboard",
    "site_brand": "Planning",
    "site_logo": "img/logo.png",  # Replace with your logo path in the static files
    "welcome_sign": "Welcome to the Planning Admin",
    "copyright": "Planning Inc.",
    "search_model": "auth.User",
    "topmenu_links": [
        # Custom links to external or internal views
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://example.com/support", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "Profile", "url": "/profile", "new_window": False},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["auth", "your_app_name"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "custom_css": "css/custom.css",  # Optional custom styles
    "custom_js": "js/custom.js",    # Optional custom scripts
    "changeform_format": "horizontal_tabs",  # Format for model edit views
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "show_ui_builder": True,  # Show UI Builder in the Admin panel
}

WSGI_APPLICATION = 'unisda_strategic_plan.wsgi.application'
LOGIN_REDIRECT_URL = '/'  
LOGIN_URL = 'user_login'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Determine if we're running in Docker (either set by Docker Compose or check environment)
#IN_DOCKER = os.environ.get('DOCKER_CONTAINER', False) == 'true'
IN_DOCKER = os.environ.get('DOCKER_CONTAINER', 'false').lower() == 'true'

# Database configuration with fallback support
# Docker container configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'planning_db',
        'USER': 'root',  # Changed from 'score' to 'root'
        'PASSWORD': '5A55wi3D!',  # Your new root password
        'HOST': 'score_db',
        'PORT': '3306',
    }
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'planning_db',       # Your MySQL database name
#        'USER': 'root',              # Your MySQL username
#        'PASSWORD': 'kapz.kapz123',  # Your MySQL password
#        'HOST': 'localhost',         # Database host, e.g., '127.0.0.1' or 'localhost'
#        'PORT': '3306',              # MySQL default port
#    }
#}
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


#static files in root dir
STATICFILES_DIRS = [BASE_DIR / "static"]  # ref our static folder
STATIC_ROOT = BASE_DIR / 'staticfiles' 

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
