<h1 style="text-align:center">Django & Apache Guide</h1>
<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

# 1. Django

Refer to <a href="https://github.com/Axect/Webtutorial/">Django Guide</a>

# 2. Apache

* ```sudo chmod a+r (a+w) folder``` - Permission Error & Operational Error
* Don't use virtualenv pythonpath - It occurs ```/static/admin``` permission error
* Use ```wsgi.py```

```python
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
```
