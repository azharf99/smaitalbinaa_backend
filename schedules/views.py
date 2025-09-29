from rest_framework import viewsets, permissions
from utils.pagination import StandardResultsSetPagination
from .models import Period, ReporterSchedule, Schedule
from .serializers import (
    PeriodSerializer, ReporterScheduleSerializer, ScheduleSerializer
)

# Create your views here.

class PeriodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schedule periods to be viewed or edited.
    """
    queryset = Period.objects.all().order_by('number', 'type')
    serializer_class = PeriodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schedules to be viewed or edited.
    """
    queryset = Schedule.objects.select_related('schedule_time', 'schedule_course__course', 'schedule_course__teacher', 'schedule_class', 'teacher').all().order_by('schedule_day', 'schedule_time__number', 'schedule_class__class_name')
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class ReporterScheduleViewSet(viewsets.ModelViewSet):
    queryset = ReporterSchedule.objects.select_related('reporter').all().order_by('schedule_day', 'schedule_time')
    serializer_class = ReporterScheduleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
