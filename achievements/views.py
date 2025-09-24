from rest_framework import viewsets

from .models import Prestasi, ProgramPrestasi
from .serializers import PrestasiSerializer, ProgramPrestasiSerializer
from utils.permissions import HasModelPermission
from utils.pagination import StandardResultsSetPagination

class PrestasiViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Prestasi instances.
    """
    queryset = Prestasi.objects.all()
    serializer_class = PrestasiSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination

class ProgramPrestasiViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing ProgramPrestasi instances.
    """
    queryset = ProgramPrestasi.objects.all()
    serializer_class = ProgramPrestasiSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination
