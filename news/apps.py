from django.apps import AppConfig
from django.core.signals import request_finished

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        import news.signals  # Ensure signals are imported and registered
