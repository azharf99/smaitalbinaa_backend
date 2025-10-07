from django.apps import AppConfig


class StudentProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_projects'


    def ready(self):
        import student_projects.signals  # noqa
