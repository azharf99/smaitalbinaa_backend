from rest_framework import viewsets, permissions
from utils.pagination import StandardResultsSetPagination
from .models import Report
from .serializers import ReportSerializer

# Create your views here.

class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows extracurricular reports to be viewed or edited.
    """
    queryset = Report.objects.select_related('extracurricular').prefetch_related('teacher', 'students').all().order_by('-report_date')
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
