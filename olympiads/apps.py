from django.apps import AppConfig


class OlympiadsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'olympiads'


    def ready(self):
        import olympiads.signals  # noqa