from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from notifications.models import Notification
from teachers.models import Teacher
from utils.middleware import get_current_user
from utils.wa import send_message_individual_from_albinaa
from .models import Tahfidz, Tilawah, Target


def get_admin_teachers():
    """Helper function to get all teachers who are superusers."""
    admin_users = User.objects.filter(is_superuser=True)
    return Teacher.objects.filter(user__in=admin_users)


@receiver(post_save, sender=Target)
def log_target_tilawah_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Target Tilawah is created or updated.
    """
    user = get_current_user()
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Target Tilawah {action.capitalize()}"
    message = f"Target Tilawah {instance.tanggal} was {action} by {user.teacher.teacher_name}."

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='info')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


@receiver(post_delete, sender=Target)
def log_target_tilawah_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Target Tilawah is deleted.
    """
    user = get_current_user()
    if not user:
        return
    
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Target Tilawah Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Target Tilawah {instance.tanggal} was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='warning')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)



@receiver(post_save, sender=Tilawah)
def log_tilawah_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Tilawah is created or updated.
    """
    user = get_current_user()
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Tilawah {action.capitalize()}"
    message = f"Tilawah {instance.tanggal} {instance.santri.student_name} was {action} by {user.teacher.teacher_name}."

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='info')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


@receiver(post_delete, sender=Tilawah)
def log_tilawah_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Tilawah is deleted.
    """
    user = get_current_user()
    if not user:
        return
    
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Tilawah Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Tilawah {instance.tanggal} {instance.santri.student_name} was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='warning')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


@receiver(post_save, sender=Tahfidz)
def log_tahfidz_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Tahfidz is created or updated.
    """
    user = get_current_user()
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Tahfidz {action.capitalize()}"
    message = f"Tahfidz {instance.santri.student_name} was {action} by {user.teacher.teacher_name}."

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='info')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


@receiver(post_delete, sender=Tahfidz)
def log_tahfidz_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Tahfidz is deleted.
    """
    user = get_current_user()
    if not user:
        return
    
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Tahfidz Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Tahfidz {instance.santri.student_name} was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='warning')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)
