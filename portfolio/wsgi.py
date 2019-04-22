"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
os.environ["EMAIL_HOST_USER"] = "help.portfolio.apps@gmail.com"
os.environ["EMAIL_HOST_PASSWORD"] = "jhvf65@Y56mrdc76d86HN"

application = get_wsgi_application()
