from rest_framework import viewsets
from utils.pagination import StandardResultsSetPagination
from utils.permissions import HasModelPermission
from .models import LaporanPertanggungJawaban, ProgramKerja
from .serializers import LaporanPertanggungJawabanSerializer, ProgramKerjaSerializer


class LaporanPertanggungJawabanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Laporan Pertanggung Jawaban (LPJ) to be viewed or edited.
    """
    queryset = LaporanPertanggungJawaban.objects.all().order_by('-tahun_ajaran', 'program')
    serializer_class = LaporanPertanggungJawabanSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination


class ProgramKerjaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Program Kerja (Proker) to be viewed or edited.
    """
    queryset = ProgramKerja.objects.all().order_by('-tahun_ajaran', 'program')
    serializer_class = ProgramKerjaSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination
