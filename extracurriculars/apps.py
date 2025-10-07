from django.apps import AppConfig


class ExtracurricularsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'extracurriculars'

    def ready(self):
        import extracurriculars.signals