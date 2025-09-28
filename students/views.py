from rest_framework import viewsets, filters
from .models import Student
from .serializers import StudentSerializer
from utils.permissions import HasModelPermission
from utils.pagination import StandardResultsSetPagination

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Student instances.
    """
    queryset = Student.objects.select_related('student_class').filter(student_status="Aktif")
    serializer_class = StudentSerializer
    permission_classes = [HasModelPermission]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['student_name', 'nis', 'nisn', 'student_class__class_name']


    def get_queryset(self):
        """Optionally filters by `user_id` query parameter."""
        class_id = self.request.GET.get('class_id')
        if class_id:
            return super().get_queryset().filter(student_class__id=class_id)
        
        return super().get_queryset()
