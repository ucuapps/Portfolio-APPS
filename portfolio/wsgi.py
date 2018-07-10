"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

os.environ["EMAIL_HOST_USER"] = "help.portfolio.apps@gmail.com"
os.environ["EMAIL_HOST_PASSWORD"] = "hgq@e13n4h"
os.environ["DATABASE_PASSWORD"] = "theLupA17kKLRPopt13k"
os.environ["DATABASE_USERNAME"] = "portfoliouser"


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")


application = get_wsgi_application()
