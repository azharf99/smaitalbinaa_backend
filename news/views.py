from datetime import timezone
from rest_framework import viewsets, permissions

from teachers.models import Teacher
from utils.pagination import StandardResultsSetPagination
from .models import Category, Post, Comment
from .serializers import CategorySerializer, PostSerializer, CommentSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    Published posts are visible to anyone, drafts are only visible to authenticated users.
    """
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]    

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    # lookup_field = 'id'

    # def perform_create(self, serializer):
    #     """
    #     Automatically associate the post with the logged-in user (teacher).
    #     """
    #     try:
    #         writer = self.request.user.teacher
    #     except:
    #         writer = Teacher.objects.get(user=1)
        
    #     # Assumes the logged-in user has a one-to-one relationship with a Teacher model.
    #     serializer.save(author=writer)

    # def update(self, request, *args, **kwargs):
    #     # Remove read-only fields from request.data to avoid validation errors
    #     if hasattr(request, 'data'):
    #         mutable = getattr(request.data, '_mutable', None)
    #         if mutable is not None:
    #             request.data._mutable = True
    #         for field in ['id', 'author', 'created_at', 'updated_at', 'comments']:
    #             request.data.pop(field, None)
    #         if mutable is not None:
    #             request.data._mutable = False
    #     return super().update(request, *args, **kwargs)

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or created.
    """
    queryset = Comment.objects.filter(active=True)
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Assuming the user is a teacher.
        # You might need to adjust this based on your user model relationship.
        serializer.save(author=self.request.user.teacher)
