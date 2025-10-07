from django.apps import AppConfig


class ExtracurricularScoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'extracurricular_scores'

    def ready(self):
        import extracurricular_scores.signals