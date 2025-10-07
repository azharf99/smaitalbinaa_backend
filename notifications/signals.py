from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from notifications.models import Notification
from teachers.models import Teacher
from utils.middleware import get_current_user
from utils.wa import send_message_individual_from_albinaa
from .models import Notification


admin_phone = settings.ADMIN_PHONE


@receiver(post_save, sender=Notification)
def log_notification_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Notification is created or updated.
    """
    user = get_current_user()
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    message = f"Notification {instance.title} was {action} by {user.teacher.teacher_name}."

    send_message_individual_from_albinaa(phone=admin_phone, message=message)


@receiver(post_delete, sender=Notification)
def log_notification_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Notification is deleted.
    """
    user = get_current_user()
    if not user:
        return
    
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Notification {instance.title} was deleted by {user.teacher.teacher_name}."
    send_message_individual_from_albinaa(phone=admin_phone, message=message)


