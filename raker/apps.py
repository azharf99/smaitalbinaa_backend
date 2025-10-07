from django.apps import AppConfig


class RakerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'raker'

    def ready(self):
        import raker.signals  # noqa