# signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from teachers.models import Teacher


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
   if created:
       Teacher.objects.create(
          user=instance,
          teacher_name=instance.first_name + ' ' + instance.last_name if instance.first_name and instance.last_name else instance.username,
          short_name=instance.first_name + ' ' + instance.last_name[0] if instance.first_name and instance.last_name else instance.username,
          email=instance.email
          )
       
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
   instance.teacher.save()