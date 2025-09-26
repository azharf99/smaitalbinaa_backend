from rest_framework import viewsets, filters

from .models import Alumni
from .serializers import AlumniSerializer
from utils.permissions import HasModelPermission
from utils.pagination import StandardResultsSetPagination


class AlumniViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Alumni instances.
    """
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'nis', 'nisn', 'group', 'city', 'province', 'undergraduate_department', 'undergraduate_university']
