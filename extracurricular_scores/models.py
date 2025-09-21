from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from extracurriculars.models import Extracurricular
from students.models import Student
from utils.constants import EXTRACURRICULAR_SCORE_CHOICES

# Create your models here.

class Score(models.Model):
    extracurricular = models.ForeignKey(Extracurricular, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.CharField(max_length=3, choices=EXTRACURRICULAR_SCORE_CHOICES, default=EXTRACURRICULAR_SCORE_CHOICES[1][0])
    semester = models.CharField(max_length=7, default=settings.SEMESTER, null=True)
    academic_year = models.CharField(max_length=20, default=settings.TAHUN_AJARAN, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} {self.extracurricular.name} {self.score} {self.semester} {self.academic_year}"


    def get_absolute_url(self):
        return reverse("nilai-list")
    
    class Meta:
        ordering = ["student", "extracurricular"]
        verbose_name = _("Score")
        verbose_name_plural = _("Scores")
        db_table = "scores"
        indexes = [
            models.Index(fields=["id",]),
        ]