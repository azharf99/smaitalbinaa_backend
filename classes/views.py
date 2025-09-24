from rest_framework import viewsets

from .models import Class
from .serializers import ClassSerializer
from utils.permissions import HasModelPermission
from utils.pagination import StandardResultsSetPagination

class ClassViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Class instances.
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination
