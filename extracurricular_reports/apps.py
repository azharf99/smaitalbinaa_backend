from django.apps import AppConfig


class ExtracurricularReportsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'extracurricular_reports'

    def ready(self):
        import extracurricular_reports.signals  # noqa

