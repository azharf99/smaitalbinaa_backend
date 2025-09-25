from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Teacher
from .serializers import UserSerializer, TeacherSerializer
from utils.permissions import HasModelPermission
from utils.pagination import StandardResultsSetPagination

class UsersViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Teacher instances.
    """
    queryset = User.objects.all()
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
