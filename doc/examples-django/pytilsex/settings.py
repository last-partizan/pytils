# Django settings for pytilsex project.

# find current path
import os

BASE_DIR = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEFAULT_CHARSET = 'utf-8'

ADMINS = (
    ('Pythy', 'the.pythy@gmail.com'),
)

DATABASES = {
    'default': {
        'NAME': 'pytils_example',
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

MANAGERS = ADMINS

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'UTC'
USE_TZ = False

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

STATICFILES_DIRS = (
    MEDIA_ROOT,
)

STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-)^ay7gz76#9!j=ssycphb7*(gg74zhx9h-(j_1k7!wfr7j(o^'


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'pytilsex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
]


INSTALLED_APPS = (
    # -- install pytils
    'pytils',
)


# is value will shown at error in pytils (default - False)
# PYTILS_SHOW_VALUES_ON_ERROR = True
