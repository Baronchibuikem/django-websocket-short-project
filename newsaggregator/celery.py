import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsaggregator.settings')

app = Celery('newsaggregator')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_joke_3sec': {
        'task': 'app_news.tasks.get_jokes',
        'schedule': 3.0
    }
}
app.autodiscover_tasks()

