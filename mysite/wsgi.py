"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from os.path import abspath, dirname, join
import sys

with open("/var/www/HEP_Web_Django.sys.path", "w")as f:
  for i in sys.path:
    f.write(i+"\n")

sys.stdout = sys.stderr

from django.core.wsgi import get_wsgi_application
from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
