from django.http import JsonResponse
from rest_framework import viewsets, permissions
from schedules.models import ReporterSchedule, Schedule
from utils.constants import WEEKDAYS_DICT
from utils.pagination import StandardResultsSetPagination
from utils.permissions import HasModelPermission
from .models import NonTeacherReport, Report
from rest_framework.decorators import api_view, permission_classes as rest_permission_classes
from .serializers import NonTeacherReportSerializer, ReportSerializer
from django.conf import settings as django_settings
from django.utils import timezone



# Create your views here.


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows class reports to be viewed or edited.
    """
    queryset = Report.objects.select_related(
        'schedule__schedule_class', 'schedule__schedule_course__course',
        'schedule__schedule_course__teacher', 'schedule__schedule_time',
        'schedule__teacher', 'subtitute_teacher', 'reporter'
    ).all().order_by('-report_date', 'schedule__schedule_time__number')
    serializer_class = ReportSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination


    def get_queryset(self):
        query_date = self.request.GET.get('date')
        if query_date:  
            self.pagination_class = None
            return super().get_queryset().filter(report_date=query_date)
        
        return super().get_queryset()


class NonTeacherReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows non-teacher reports to be viewed or edited.
    """
    queryset = NonTeacherReport.objects.select_related('teacher', 'schedule_time').all().order_by('-report_date', 'schedule_time__number')
    serializer_class = NonTeacherReportSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination

@api_view(['POST'])
@rest_permission_classes([permissions.IsAdminUser])
def generate_report_by_date(request):
    """
    Generate reports for a given date based on existing schedules.
    Expects a 'date' in 'YYYY-MM-DD' format in the POST data.
    If 'date' is not provided, it defaults to the current date.
    """
    try:
        search_date_str = request.data.get('date')
        if search_date_str:
            report_date = timezone.datetime.strptime(search_date_str, '%Y-%m-%d').date()
        else:
            report_date = timezone.now().date()
    except (ValueError, TypeError):
        return JsonResponse({'error': "Invalid date format. Use YYYY-MM-DD."}, status=400)

    day_of_week = WEEKDAYS_DICT.get(report_date.isoweekday())
    if not day_of_week:
        return JsonResponse({'message': 'No schedules for this day of the week.'}, status=200)

    # We can add filtering by type (e.g. 'Putra', 'Putri') if needed
    schedules_for_day = Schedule.objects.prefetch_related('schedule_time').filter(schedule_day=day_of_week)

    reports_to_create = [
        Report(
            report_date=report_date,
            reporter = ReporterSchedule.objects.select_related('reporter').filter(schedule_time=str(schedule.schedule_time.number), schedule_day=day_of_week).first().reporter or None,
            schedule=schedule,
            semester=django_settings.SEMESTER,
            academic_year=django_settings.TAHUN_AJARAN,
        )
        for schedule in schedules_for_day
    ]

    created_reports = Report.objects.bulk_create(reports_to_create, ignore_conflicts=True)
    
    return JsonResponse({'message': f'{len(created_reports)} reports created successfully for {report_date}.'}, status=201)



@api_view(['POST'])
@rest_permission_classes([permissions.IsAdminUser])
def set_current_reporter(request):
    """
    Generate reports for a given date based on existing schedules.
    Expects a 'date' in 'YYYY-MM-DD' format in the POST data.
    If 'date' is not provided, it defaults to the current date.
    """
    try:
        search_date_str = request.data.get('date')
        if search_date_str:
            time_no = request.data.get('time_no')
            reporter_id = request.data.get('reporter_id')
            report_date = timezone.datetime.strptime(search_date_str, '%Y-%m-%d').date()
        else:
            return JsonResponse({'error': "Invalid date format. Use YYYY-MM-DD."}, status=400)
    except (ValueError, TypeError):
        return JsonResponse({'error': "Invalid date format. Use YYYY-MM-DD."}, status=400)

    day_of_week = WEEKDAYS_DICT.get(report_date.isoweekday())
    if not day_of_week:
        return JsonResponse({'message': 'No schedules for this day of the week.'}, status=200)

    # We can add filtering by type (e.g. 'Putra', 'Putri') if needed
    report_objects = Report.objects.filter(report_date=report_date, schedule__schedule_time__number=time_no)
    report_objects.update(reporter_id=reporter_id, is_submitted=True)
    is_completed = True
    for obj in report_objects:
        if obj.status != "Hadir":
            is_completed = False
            break
    report_objects.update(is_complete=is_completed)

    
    return JsonResponse({'message': f'Reporter for {report_date} and time {time_no} reports updated successfully.'}, status=201)