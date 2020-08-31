"""
ASGI config for dashboard project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Load the correct environment
ENVIRONMENT = 'base'
try:
    from dashboard.settings.env import *
except ImportError:
    pass

config = 'dashboard.settings.' + ENVIRONMENT
os.environ.setdefault('DJANGO_SETTINGS_MODULE', config)
os.environ.setdefault('DJANGO_CONFIGURATION', config)

application = get_asgi_application()
