from rest_framework import viewsets

from .models import Teacher
from .serializers import TeacherSerializer
from utils.permissions import HasModelPermission
from utils.pagination import StandardResultsSetPagination

class TeacherViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Teacher instances.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination
