from rest_framework import viewsets
from utils.pagination import StandardResultsSetPagination
from .models import AcademicCalendar
from utils.permissions import HasModelPermission
from .serializers import AcademicCalendarSerializer

class AcademicCalendarViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing AcademicCalendar instances.

    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions.
    """
    queryset = AcademicCalendar.objects.all()
    serializer_class = AcademicCalendarSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [HasModelPermission]
