import os
import sys
path = '/var/www/HEP_Web_Django'
if path not in sys.path:
  sys.path.append(path)
sys.path.append('/var/www/HEP_Web_Django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mysite.settings')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
