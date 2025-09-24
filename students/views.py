from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializer
from utils.permissions import HasModelPermission
from utils.pagination import StandardResultsSetPagination

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination
