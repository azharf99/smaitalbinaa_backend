# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CategoryViewSet, PostViewSet, CommentViewSet

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet, basename='category')
# router.register(r'posts', PostViewSet, basename='post')
# router.register(r'comments', CommentViewSet, basename='comment')
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, CreateView
from django.urls import path, include

class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

class NewsCreateView(CreateView):
    model = Post
    template_name = 'news/create_news.html'
    fields = ['title', 'content', 'category']
    success_url = '/news/'


urlpatterns = [
    # path('', include(router.urls)),
    path('', NewsListView.as_view(), name='news-list'),
    path('create/', NewsCreateView.as_view(), name='news-create'),
]