from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from utils.constants import GENDER_CHOICES

# Create your models here.
class AcademicCalendar(models.Model):
    event_name = models.CharField(_("Nama Event"), max_length=50)
    event_start_date = models.DateField(_("Tanggal Mulai Event"))
    event_end_date = models.DateField(_("Tanggal Berakhir Event"), null=True, blank=True)
    description = models.CharField(_("Deskripsi"), max_length=1000, blank=True, null=True)
    category = models.CharField(_("Kategori"), max_length=50, blank=True, null=True)
    type = models.CharField(_("Tipe"), max_length=20, choices=GENDER_CHOICES, default=GENDER_CHOICES[1][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.event_name} | {self.event_start_date}"
    

    def get_absolute_url(self):
        return reverse("calendar-list")
    

    class Meta:
        ordering = ["event_name"]
        verbose_name = _("Academic Calendar")
        verbose_name_plural = _("Academic Calendars")
        db_table = "academic_calendar"
        indexes = [
            models.Index(fields=["id", "event_name", "event_start_date"]),
        ]
    


