import os
import django
from celery import Celery
from influencers_app.tasks import SCHEDULE as INFLUENCERS_APP_SCHEDULE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'influencers.settings')
django.setup()
app = Celery('influencers')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = INFLUENCERS_APP_SCHEDULE

app.autodiscover_tasks()
