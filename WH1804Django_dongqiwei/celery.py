from __future__ import absolute_import

import os
from celery import Celery
from WH1804Django_dongqiwei import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WH1804Django_dongqiwei.settings')

app = Celery('WH1804Django_dongqiwei', backend='redis', broker=settings.CELERY_BROKER_URL)

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
