"""
URL configuration for smaitalbinaa_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.flatpages.views import flatpage
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from academic_calendar.views import AcademicCalendarViewSet
from achievements.views import PrestasiViewSet, ProgramPrestasiViewSet
from alumni.views import AlumniViewSet
from classes.views import ClassViewSet
from courses.views import CourseViewSet, SubjectViewSet
from news.views import CategoryViewSet, CommentViewSet, ImageUploadView, PostViewSet
from tahfidz.views import TahfidzViewSet, TargetViewSet, TilawahViewSet
from teachers.views import TeacherViewSet, UsersViewSet
from students.views import StudentViewSet
from utils.login import exchange_token
from utils.views import MyTokenObtainPairView


router = DefaultRouter()
router.register(r'academic-calendars', AcademicCalendarViewSet, basename='academiccalendar')
router.register(r'achievements', PrestasiViewSet, basename='prestasi')
router.register(r'achievements-program', ProgramPrestasiViewSet, basename='programprestasi')
router.register(r'classes', ClassViewSet, basename='class')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'users', UsersViewSet, basename='user')
router.register(r'alumni', AlumniViewSet, basename='alumni')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'tahfidz', TahfidzViewSet, basename='tahfidz')
router.register(r'targets', TargetViewSet, basename='target')
router.register(r'tilawah', TilawahViewSet, basename='tilawah')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('api/v1/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/exchange-token/', exchange_token, name='token_exchange'),    
    path('api/v1/tahfidz-app/', include('tahfidz.urls')),
    path('upload/', ImageUploadView.as_view(), name='ckeditor_upload'),
    
]


if settings.DEBUG:
    urlpatterns = [
        *urlpatterns,
        path("__debug__/", include("debug_toolbar.urls")),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    path("about-us/", flatpage, {"url": "/about-us/"}, name="about"),
    path("license/", flatpage, {"url": "/license/"}, name="license"),
]