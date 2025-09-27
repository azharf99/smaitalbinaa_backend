from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurahListView, TahfidzViewSet, TargetViewSet, TilawahQuickCreateView, TilawahViewSet

router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('tilawah/quick-create/', TilawahQuickCreateView.as_view(), name='tilawah-quick-create'),
    path('surahs/', SurahListView.as_view(), name='surah-list'),
]