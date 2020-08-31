#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Load the correct environment
ENVIRONMENT = 'base'
try:
    from dashboard.settings.env import *
except ImportError:
    pass


def main():
    config = 'dashboard.settings.' + ENVIRONMENT
    os.environ['DJANGO_SETTINGS_MODULE'] = config
    os.environ['DJANGO_CONFIGURATION'] = config
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', config)
    # os.environ.setdefault('DJANGO_CONFIGURATION', config)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
