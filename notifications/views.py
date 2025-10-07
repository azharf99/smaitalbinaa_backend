from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from teachers.models import Teacher
from utils.pagination import StandardResultsSetPagination
from utils.permissions import HasModelPermission
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notifications to be viewed or edited.
    """
    serializer_class = NotificationSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        This view should return a list of all the notifications
        for the currently authenticated user.
        """
        user = self.request.user
        try:
            teacher = user.teacher
            return Notification.objects.filter(teacher=teacher)
        except Teacher.DoesNotExist:
            return Notification.objects.none()


    @action(detail=True, methods=['patch'], url_path='mark-read')
    def mark_as_read(self, request, pk=None):
        """Mark a single notification as read."""
        notification = self.get_object()
        notification.is_read = True
        notification.save(update_fields=['is_read'])
        serializer = self.get_serializer(notification)
        return Response(serializer.data)

    @action(detail=False, methods=['patch'], url_path='mark-all-read')
    def mark_all_as_read(self, request):
        """Mark all notifications for the current user as read."""
        self.get_queryset().update(is_read=True)
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=False, methods=['post'], url_path='batch-create')
    def batch_create_notifications(self, request):
        data = request.data
        teachers = Teacher.objects.filter(status='Aktif')
        
        notifications = []
        for teacher in teachers:
            notification = Notification.objects.create(
                teacher=teacher,
                title=data['title'],
                message=data['message'],
                type=data['type']
            )
            notifications.append(notification)
        
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=201)