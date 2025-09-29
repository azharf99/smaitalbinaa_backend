from rest_framework import viewsets, permissions
from utils.pagination import StandardResultsSetPagination
from .models import Score
from .serializers import ScoreSerializer

# Create your views here.

class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows extracurricular scores to be viewed or edited.
    """
    queryset = Score.objects.select_related('student', 'extracurricular').all().order_by('student', 'extracurricular')
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
