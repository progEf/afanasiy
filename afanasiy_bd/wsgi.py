"""
WSGI config for afanasiy_bd project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.contrib import admin

from django.core.wsgi import get_wsgi_application

from afas.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'afanasiy_bd.settings')

application = get_wsgi_application()



