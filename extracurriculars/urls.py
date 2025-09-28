from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExtracurricularViewSet

router = DefaultRouter()
router.register(r'', ExtracurricularViewSet, basename='extracurricular')

urlpatterns = [
    path('', include(router.urls)),
]