from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from notifications.models import Notification
from teachers.models import Teacher
from utils.middleware import get_current_user
from utils.wa import send_message_individual_from_albinaa
from .models import Project, Team, DailyPlan


def get_admin_teachers():
    """Helper function to get all teachers who are superusers."""
    admin_users = User.objects.filter(is_superuser=True)
    return Teacher.objects.filter(user__in=admin_users)


@receiver(post_save, sender=Team)
def log_team_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Team is created or updated.
    """
    user = get_current_user()
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Team {action.capitalize()}"
    message = f"Team {instance.team_leader.student_name} was {action} by {user.teacher.teacher_name}."

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='info')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


@receiver(post_delete, sender=Team)
def log_team_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Team is deleted.
    """
    user = get_current_user()
    if not user:
        return
    
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Team Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Team {instance.team_leader.student_name} was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='warning')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)



@receiver(post_save, sender=Project)
def log_project_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Project is created or updated.
    """
    user = get_current_user()
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Project {action.capitalize()}"
    message = f"Project {instance.project_name} was {action} by {user.teacher.teacher_name}."

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='info')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


@receiver(post_delete, sender=Project)
def log_project_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Project is deleted.
    """
    user = get_current_user()
    if not user:
        return
    
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Project Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Project {instance.project_name} was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='warning')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


@receiver(post_save, sender=DailyPlan)
def log_daily_plan_change(sender, instance, created, **kwargs):
    """
    Create a notification when a Daily Plan is created or updated.
    """
    user = get_current_user()
    if not user:
        return  # Do nothing if the action was not performed by a user (e.g., in a shell)
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile

    action = "created" if created else "updated"
    title = f"Daily Plan {action.capitalize()}"
    message = f"Daily Plan {instance.date} {instance.project.project_name} was {action} by {user.teacher.teacher_name}."

    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='info')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


@receiver(post_delete, sender=DailyPlan)
def log_daily_plan_deletion(sender, instance, **kwargs):
    """
    Create a notification when a Daily Plan is deleted.
    """
    user = get_current_user()
    if not user:
        return
    
    if not hasattr(user, 'teacher'):
        return  # Do nothing if the user has no associated teacher profile
    
    title = "Daily Plan Deleted"
    # Use user.teacher.teacher_name for consistency and to avoid potential errors if user has no teacher profile.
    message = f"Daily Plan {instance.date} {instance.project.project_name} was deleted by {user.teacher.teacher_name}."
    
    # Create notifications for all admin teachers
    admin_teachers = get_admin_teachers()
    notifications_to_create = [
        Notification(teacher=teacher, title=title, message=message, type='warning')
        for teacher in admin_teachers
    ]
    Notification.objects.bulk_create(notifications_to_create)
    send_message_individual_from_albinaa(phone=user.teacher.phone, message=message)


