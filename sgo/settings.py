"""
Django settings for sgo project.

Generated by 'django-admin startproject' using Django 5.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!xx(&d-*kcx+c*7++5o0#x+o#-815hx78o)eau_l33ybd=zyjt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # Administração do Django.
    'django.contrib.auth',  # Autenticação.
    'django.contrib.contenttypes',  # Framework de tipos de conteúdo.
    'django.contrib.sessions',  # Gerenciamento de sessões.
    'django.contrib.messages',  # Sistema de mensagens.
    'django.contrib.staticfiles',  # Gerenciamento de arquivos estáticos.
    'core',  
    'tratamentos',
    'index',
    'planos',
    'sobrenos',
    'contatos',
    'consulta',
    'cadastro',
    'cadastro_adm',
    'cadastro_registro',
    'esqueceu_senha',
    'config',
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

ROOT_URLCONF = 'sgo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Motor de template do Django.
        'DIRS': ['templates'],  # Diretório de templates personalizados.
        'APP_DIRS': True,  # Django procura templates dentro de cada aplicação.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Adiciona variáveis de depuração.
                'django.template.context_processors.request',  # Adiciona 'request' ao contexto dos templates.
                'django.contrib.auth.context_processors.auth',  # Adiciona variáveis relacionadas à autenticação.
                'django.contrib.messages.context_processors.messages',  # Adiciona mensagens ao contexto dos templates.
                'sgo.context_processors.paciente_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'sgo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Define o tempo que a sessão permanecerá ativa antes de expirar (em segundos)
SESSION_COOKIE_AGE = 86400  # 1 dia
SESSION_SAVE_EVERY_REQUEST = True  # Salva a sessão a cada request, estendendo o tempo de expiração

# settings.py
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # ou outro backend de sessão, dependendo do seu caso


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'pt-br'  # Código da língua.
TIME_ZONE = 'America/Sao_Paulo'  # Fuso horário.
USE_I18N = True  # Habilita internacionalização.
USE_TZ = True  # Habilita suporte a fuso horário.

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Caminho onde os arquivos estáticos serão coletados
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Diretório para coletar os arquivos estáticos



# settings.py

LOGIN_REDIRECT_URL = 'index_cliente'  # Redireciona para a URL após login bem-sucedido
LOGOUT_REDIRECT_URL = 'index'  # Redireciona para a URL após logout
# settings.py
LOGIN_URL = '/cadastro/login/'  # Ajuste essa URL para o caminho correto da página de login






# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'   # Altere para o seu servidor SMTP
EMAIL_PORT = 587                       # Geralmente 587 para TLS, ou 465 para SSL
EMAIL_USE_TLS = True                   # Altere para True se estiver usando TLS
EMAIL_HOST_USER = 'sorrisodasgracas@gmail.com'
EMAIL_HOST_PASSWORD = 'cjcc fyex dfpv fgkl'      # Certifique-se de não compartilhar sua senha
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER 