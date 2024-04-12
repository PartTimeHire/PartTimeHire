from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-x9vf4aeprso6u6rt@sk_fos#-=ygj@^b--&!84-vqm0u6#7uq2'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Add if not already present

    # Third-party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # Your app
    'django_project',  # Add your app here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Add print statements in this middleware
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]




ROOT_URLCONF = 'django_project.urls'

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

WSGI_APPLICATION = 'django_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Add the following configurations for django-allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server address
EMAIL_PORT = 587  # Gmail server port
EMAIL_USE_TLS = True  # Use TLS encryption for security

# Replace these with your actual Gmail credentials
EMAIL_HOST_USER = 'jaddjamesjd@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'Qwqwqwqw17!'  # Your email password or app-specific password

# Redirect to home URL after login
LOGIN_REDIRECT_URL = '/'

# Redirect to home URL after logout
LOGOUT_REDIRECT_URL = '/'

# Redirect to this URL after successful signup
ACCOUNT_SIGNUP_REDIRECT_URL = '/verification/'  # Change '/verification/' to your desired URL

# Ensure that users are redirected to the home page after successful login
ACCOUNT_SIGNUP_REDIRECT_URL = LOGIN_REDIRECT_URL

# Require email verification before login
ACCOUNT_EMAIL_REQUIRED = True

# Specify the email verification method
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
