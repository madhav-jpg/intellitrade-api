"""
WSGI config for market_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = "market_api.deployment" if "WEBSITE_HOSTNAME" in os.environ else "market_api.settings"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market_api.deployment")

application = get_wsgi_application()