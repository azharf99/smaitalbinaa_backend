import csv
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Extracurricular
from .serializers import ExtracurricularSerializer
from utils.permissions import HasModelPermission
from utils.pagination import StandardResultsSetPagination
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
import io
from django.db import transaction
from teachers.models import Teacher
from students.models import Student
from rest_framework.decorators import action


class ExtracurricularViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Extracurricular instances.
    """
    queryset = Extracurricular.objects.prefetch_related('teacher', 'members', 'members__student_class').all().order_by('name')
    serializer_class = ExtracurricularSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'type': ['exact'],
        'category': ['exact'],
        'status': ['exact'],
    }

    def get_queryset(self):
        """Optionally filters by `search` query parameter on the `name` field."""
        search_query = self.request.GET.get('search')
        id_query = self.request.GET.get('id')
        all_extracurriculars = self.request.GET.get('all')
        
        queryset = super().get_queryset()
        if all_extracurriculars == "true":
            self.pagination_class = None
            return queryset.filter(status="Aktif")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query, status="Aktif")
        if id_query:
            queryset = queryset.filter(id=id_query)
        return queryset
    

    @action(detail=False, methods=['get'])
    def export(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="extracurriculars.csv"'

        writer = csv.writer(response)
        # Define CSV headers
        headers = [
            'id', 'name', 'short_name', 'schedule', 'time', 
            'type', 'category', 'status', 'teachers', 'members_count'
        ]
        writer.writerow(headers)

        # Get all extracurriculars
        queryset = self.get_queryset()

        for extra in queryset:
            teachers = ", ".join([t.teacher_name for t in extra.teacher.all()])
            members_count = extra.members.count()
            
            writer.writerow([
                extra.id,
                extra.name,
                extra.short_name,
                extra.schedule,
                extra.time,
                extra.type,
                extra.category,
                extra.status,
                teachers,
                members_count
            ])

        return response


    # /api/v1/extracurriculars/import/

    @action(detail=False, methods=['post'], parser_classes=[MultiPartParser], url_path='import')
    def import_csv(self, request, *args, **kwargs):
        file_obj = request.data.get('file')

        if not file_obj:
            return Response({"detail": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)
        if not file_obj.name.endswith('.csv'):
            return Response({"detail": "File must be a CSV."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_file = file_obj.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            # Use DictReader to easily access columns by name
            reader = csv.DictReader(io_string)

            with transaction.atomic():
                for row in reader:
                    name = row.get('name')
                    if not name:
                        continue # Skip rows without a name

                    # Create or update the extracurricular object
                    extra, created = Extracurricular.objects.update_or_create(
                        name=name,
                        defaults={
                            'short_name': row.get('short_name'),
                            'schedule': row.get('schedule'),
                            'time': row.get('time'),
                            'description': row.get('description'),
                            'type': row.get('type'),
                            'category': row.get('category'),
                            'status': row.get('status', 'Aktif'),
                        }
                    )

                    # Handle Many-to-Many for teachers
                    teacher_ids_str = row.get('teacher_ids', '')
                    if teacher_ids_str:
                        teacher_ids = [int(id.strip()) for id in teacher_ids_str.split(',') if id.strip().isdigit()]
                        teachers = Teacher.objects.filter(id__in=teacher_ids)
                        extra.teacher.set(teachers)

                    # Handle Many-to-Many for members
                    member_ids_str = row.get('member_ids', '')
                    if member_ids_str:
                        member_ids = [int(id.strip()) for id in member_ids_str.split(',') if id.strip().isdigit()]
                        members = Student.objects.filter(id__in=member_ids)
                        extra.members.set(members)

        except Exception as e:
            return Response({"detail": f"An error occurred during import: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Extracurriculars imported successfully."}, status=status.HTTP_201_CREATED)
