# signals.py
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from notifications.models import Notification
from utils.middleware import get_current_user
from teachers.models import Teacher
from utils.wa import send_message_individual_from_albinaa

def get_admin_teachers():
    """Helper function to get all teachers who are superusers."""
    admin_users = User.objects.filter(is_superuser=True)
    return Teacher.objects.filter(user__in=admin_users)


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


@receiver(post_save, sender=Teacher)
def log_tahfidz_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Teacher is created or updated.
    """
    user = get_current_user()
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Teacher {action.capitalize()}"
    message = f"Teacher {instance.teacher_name} was {action} by {user.teacher.teacher_name}."

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='info')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


@receiver(post_delete, sender=Teacher)
def log_tahfidz_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Teacher is deleted.
    """
    user = get_current_user()
    if not user:
        return
    
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Teacher Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Teacher {instance.teacher_name} was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='warning')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)
