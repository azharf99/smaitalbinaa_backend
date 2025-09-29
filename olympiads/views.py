from rest_framework import viewsets, permissions
from utils.pagination import StandardResultsSetPagination
from .models import OlympiadField, OlympiadReport
from .serializers import OlympiadFieldSerializer, OlympiadReportSerializer

# Create your views here.

class OlympiadFieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows olympiad fields to be viewed or edited.
    """
    queryset = OlympiadField.objects.select_related('teacher').prefetch_related('members').all().order_by('type', 'field_name')
    serializer_class = OlympiadFieldSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class OlympiadReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows olympiad reports to be viewed or edited.
    """
    queryset = OlympiadReport.objects.select_related('field_name').prefetch_related('students').all().order_by('-report_date')
    serializer_class = OlympiadReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

