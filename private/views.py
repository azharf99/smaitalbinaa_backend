from rest_framework import viewsets, permissions
from utils.pagination import StandardResultsSetPagination
from .models import Subject, Group, Private
from .serializers import SubjectSerializer, GroupSerializer, PrivateSerializer

# Create your views here.

class PrivateSubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows private lesson subjects to be viewed or edited.
    """
    queryset = Subject.objects.prefetch_related('pembimbing').all().order_by('nama_pelajaran')
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows private lesson groups to be viewed or edited.
    """
    queryset = Group.objects.select_related('pelajaran').all().order_by('nama_kelompok')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class PrivateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows private lesson records to be viewed or edited.
    """
    queryset = Private.objects.select_related('pembimbing', 'pelajaran', 'kelompok').prefetch_related('kehadiran_santri').all().order_by('-tanggal_bimbingan')
    serializer_class = PrivateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        # Automatically set the 'pembimbing' to the currently logged-in user's teacher profile
        if hasattr(self.request.user, 'teacher'):
            serializer.save(pembimbing=self.request.user.teacher)
        else:
            # Handle cases where the user is not a teacher or has no teacher profile
            # For now, we'll let it proceed and rely on serializer validation
            serializer.save()
