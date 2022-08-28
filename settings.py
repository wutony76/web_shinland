import os

ROOT_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shinland_dev',
        'USER': 'neodev',
        'PASSWORD': '2wsx3edc',
        'HOST': '192.168.1.199',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Taipei'
LANGUAGE_CODE = 'zh-tw'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.abspath(os.path.join(ROOT_PATH, '../', 'shinland_media'))
MEDIA_URL = ''

STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
		('css', os.path.join(STATIC_ROOT, 'css')),
		('images', os.path.join(STATIC_ROOT, 'images')),
		('js', os.path.join(STATIC_ROOT, 'js')),
		('jwysiwyg', os.path.join(STATIC_ROOT, 'jwysiwyg')),
		('facebox', os.path.join(STATIC_ROOT, 'facebox')),
		('admin', os.path.join(STATIC_ROOT, 'admin')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'hr48j98@towgl+8xsb5&bz&)oa8ty!g84%mpxw=b#968n(-=66'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
		'language.middleware.LocaleMiddleware',
		'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'shinland.urls'

TEMPLATE_DIRS = (
		os.path.join(ROOT_PATH, 'templates'),
		os.path.join(ROOT_PATH, 'admin', 'templates'),
)

INSTALLED_APPS = (
		'admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
		'django.contrib.admin',
		'about',
		'account',
		'album',
		'contactus',
		'guestbook',
		'language',
		'news',
		'pictures',
		'profiles',
		'pagination',
		'share',
		'mediacleanup',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
	"django.contrib.messages.context_processors.messages",
	'django.core.context_processors.request',
	'shinland.context_processors.static',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

FORMAT_MODULE_PATH = 'shinland.formats'
AUTH_PROFILE_MODULE = 'profiles.Profile'

#5 hours
SESSION_COOKIE_AGE = 18000
