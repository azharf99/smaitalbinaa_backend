from datetime import timezone
import json
import os

from django.conf import settings
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from teachers.models import Teacher
from utils.pagination import StandardResultsSetPagination
from .models import Category, Post, Comment
from .serializers import CategorySerializer, PostSerializer, CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    Published posts are visible to anyone, drafts are only visible to authenticated users.
    """
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]    
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'author': ['exact'],
        'category': ['exact'],
        'status': ['exact'],
        'slug': ['exact'],
    }


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or created.
    """
    queryset = Comment.objects.filter(active=True).order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        """Optionally filters by `page_id` query parameter."""
        post_id = self.request.GET.get('post')
        if post_id:
            return super().get_queryset().filter(post=post_id)
        
        return super().get_queryset()


class ImageUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('upload')

        if not image_file:
            return Response({'error': 'No image provided.'}, status=400)

        # Basic validation (you might want to extend this)
        if not image_file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            return Response({'error': 'Invalid image format.'}, status=400)

        # Save the image (you might want to use a specific storage or naming strategy)
        file_name = os.path.join(settings.CKEDITOR_UPLOAD_PATH, image_file.name)
        with open(os.path.join(settings.MEDIA_ROOT, file_name), 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        return Response({'url': os.path.join(settings.MEDIA_URL, file_name)})
