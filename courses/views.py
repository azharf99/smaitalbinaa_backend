from rest_framework import viewsets, permissions, status
import csv
import io
from django_filters.rest_framework import DjangoFilterBackend
from utils.pagination import StandardResultsSetPagination
from .models import Course, Subject
from .serializers import CourseSerializer, SubjectSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows course subjects to be viewed or edited.
    """
    queryset = Subject.objects.all().order_by('name')
    serializer_class = SubjectSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=['post'], parser_classes=[MultiPartParser])
    def import_csv(self, request, *args, **kwargs):
        file_obj = request.data.get('file')

        if not file_obj:
            return Response({"detail": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

        if not file_obj.name.endswith('.csv'):
            return Response({"detail": "File must be a CSV."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_file = file_obj.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.DictReader(io_string)

            subjects_to_create = []
            for row in reader:
                # Basic validation
                if not row.get('name') or not row.get('short_name'):
                    # You might want more robust error handling here
                    continue
                
                subjects_to_create.append(
                    Subject(
                        name=row.get('name'),
                        short_name=row.get('short_name'),
                        category=row.get('category', 'Umum'),
                        type=row.get('type', 'Putra'),
                        status=row.get('status', 'Aktif')
                    )
                )
            
            Subject.objects.bulk_create(subjects_to_create)

        except Exception as e:
            return Response({"detail": f"An error occurred during import: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Subjects imported successfully."}, status=status.HTTP_201_CREATED)


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    Provides filtering by class, teacher, and type.
    """
    queryset = Course.objects.select_related('course', 'teacher', 'class_assigned').all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['class_assigned', 'teacher', 'type']
