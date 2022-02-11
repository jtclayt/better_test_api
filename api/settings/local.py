from .base import *
from core.clients.keyvault_client import KeyVaultClient

kv_client = KeyVaultClient()
django_secret = kv_client.get_secret("SecretKey")
db_name = kv_client.get_secret("DBName")
db_user = kv_client.get_secret("DBConnectionId")
db_secret = kv_client.get_secret("DBConnectionSecret")
db_host = kv_client.get_secret("DBHost")
ai_connection_string = kv_client.get_secret("AppInsightsConnectionString")


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = django_secret

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_secret,
        'HOST': db_host,
        'PORT': 1433,
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'host_is_server': True
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db'
    }
}

# Application insights configuration
OPENCENSUS = {
    'TRACE': {
        'SAMPLER': 'opencensus.trace.samplers.ProbabilitySampler(rate=1)',
        'EXPORTER': f'''opencensus.ext.azure.trace_exporter.AzureExporter(
                  connection_string='{ai_connection_string}',
        )''',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s - %(processName)s - %(name)s\n%(message)s',
        },
    },
    'handlers': {
        'azure': {
            'class': 'opencensus.ext.azure.log_exporter.AzureLogHandler',
            'formatter': 'default',
            'connection_string': ai_connection_string
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        'polls': {
            'handlers': ['azure', 'console'],
            'level':'DEBUG'
        },
    }
}
