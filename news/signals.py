from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from notifications.models import Notification
from teachers.models import Teacher
from utils.middleware import get_current_user
from .models import Post, Category, Comment


def get_admin_teachers():
    """Helper function to get all teachers who are superusers."""
    admin_users = User.objects.filter(is_superuser=True)
    return Teacher.objects.filter(user__in=admin_users)



@receiver(post_save, sender=Post)
def log_post_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Post is created or updated.
    """
    user = get_current_user()
    print(user)
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Post {action.capitalize()}"
    message = f"Post '{instance.title}' was {action} by {user.teacher.teacher_name}."
    print(action, title, message)

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='INFO')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)


@receiver(post_delete, sender=Post)
def log_post_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Post is deleted.
    """
    user = get_current_user()
    if not user:
        return
    
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Post Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Post '{instance.title}' was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='WARNING')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)



@receiver(post_save, sender=Comment)
def log_post_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Comment is created or updated.
    """
    user = get_current_user()
    print(user)
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Comment {action.capitalize()}"
    message = f"Comment {instance.body} on post'{instance.post.title}' was {action} by {user.teacher.teacher_name}."
    print(action, title, message)

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='INFO')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)


@receiver(post_delete, sender=Comment)
def log_post_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Comment is deleted.
    """
    user = get_current_user()
    if not user:
        return
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Comment Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Comment {instance.body} on post '{instance.post.title}' was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='WARNING')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)

@receiver(post_save, sender=Category)
def log_post_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Category is created or updated.
    """
    user = get_current_user()
    print(user)
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Category {action.capitalize()}"
    message = f"Category '{instance.name}' was {action} by {user.teacher.teacher_name}."
    print(action, title, message)

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='INFO')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)


@receiver(post_delete, sender=Category)
def log_post_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Category is deleted.
    """
    user = get_current_user()
    if not user:
        return
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Category Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Category '{instance.name}' was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='WARNING')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)