from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Teacher
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import UserSerializer, TeacherSerializer
from utils.permissions import HasModelPermission
from utils.pagination import StandardResultsSetPagination

class UsersViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Teacher instances.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination


class TeacherViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Teacher instances.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'user': ['exact'],
        'status': ['exact'],
    }

    def get_queryset(self):
        """Optionally filters by `user_id` query parameter."""
        search_query = self.request.GET.get('search')
        type_query = self.request.GET.get('type')
        if search_query:
            return super().get_queryset().filter(teacher_name__icontains=search_query)
        if type_query == 'putra':
            self.pagination_class = None
            return super().get_queryset().filter(gender='L')
        if type_query == 'putri':
            self.pagination_class = None
            return super().get_queryset().filter(gender='P')
        
        return super().get_queryset()
