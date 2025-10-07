from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from notifications.models import Notification
from teachers.models import Teacher
from utils.middleware import get_current_user
from utils.wa import send_message_individual_from_albinaa
from .models import Score


def get_admin_teachers():
    """Helper function to get all teachers who are superusers."""
    admin_users = User.objects.filter(is_superuser=True)
    return Teacher.objects.filter(user__in=admin_users)


@receiver(post_save, sender=Score)
def log_extracurricular_score_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Extracurricular Score is created or updated.
    """
    user = get_current_user()
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Extracurricular Score {action.capitalize()}"
    message = f"Extracurricular Score {instance.student.student_name} {instance.extracurricular.name} was {action} by {user.teacher.teacher_name}."

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='info')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


@receiver(post_delete, sender=Score)
def log_extracurricular_score_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Extracurricular Score is deleted.
    """
    user = get_current_user()
    if not user:
        return
    
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Extracurricular Score Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Extracurricular Score {instance.student.student_name} {instance.extracurricular.name} was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='warning')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


