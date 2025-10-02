from rest_framework import viewsets, permissions
from blog_test.models import BlogTest, Caterogytest
from utils.pagination import StandardResultsSetPagination
from .serializers import BlogTestSerializer, CaterogytestSerializer
# Create your views here.

class CaterogytestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Caterogytest.objects.all()
    serializer_class = CaterogytestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class BlogTestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    Published posts are visible to anyone, drafts are only visible to authenticated users.
    """
    queryset = BlogTest.objects.all()
    serializer_class = BlogTestSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]    
    pagination_class = StandardResultsSetPagination