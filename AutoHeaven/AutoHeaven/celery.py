from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AutoHeaven.settings')

# Create the Celery app.
app = Celery('AutoHeaven')

# Configure Celery using settings in `settings.py` with the prefix `CELERY_`.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in installed apps.
app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')