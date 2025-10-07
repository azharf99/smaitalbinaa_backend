from rest_framework import viewsets, permissions
from utils.pagination import StandardResultsSetPagination
from utils.permissions import HasModelPermission
from .models import Subject, Group, Private
from .serializers import SubjectSerializer, GroupSerializer, PrivateSerializer

# Create your views here.

class PrivateSubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows private lesson subjects to be viewed or edited.
    """
    queryset = Subject.objects.prefetch_related('pembimbing').all().order_by('nama_pelajaran')
    serializer_class = SubjectSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows private lesson groups to be viewed or edited.
    """
    queryset = Group.objects.select_related('pelajaran').all().order_by('nama_kelompok')
    serializer_class = GroupSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination


class PrivateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows private lesson records to be viewed or edited.
    """
    queryset = Private.objects.select_related('pembimbing', 'pelajaran', 'kelompok').prefetch_related('kehadiran_santri').all().order_by('-tanggal_bimbingan')
    serializer_class = PrivateSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination