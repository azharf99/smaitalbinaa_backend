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
from blog_test.views import BlogTestViewSet, CaterogytestViewSet
from class_reports.views import NonTeacherReportViewSet, ReportViewSet as ClassReportViewSet, generate_report_by_date, set_current_reporter
from alumni.views import AlumniViewSet
from classes.views import ClassViewSet
from courses.views import CourseViewSet, SubjectViewSet
from extracurriculars.views import ExtracurricularViewSet
from extracurricular_reports.views import ReportViewSet
from extracurricular_scores.views import ScoreViewSet
from news.views import CategoryViewSet, CommentViewSet, ImageUploadView, PostViewSet
from notifications.views import NotificationViewSet
from olympiads.views import OlympiadFieldViewSet, OlympiadReportViewSet
from raker.views import LaporanPertanggungJawabanViewSet, ProgramKerjaViewSet
from schedules.views import PeriodViewSet, ReporterScheduleViewSet, ScheduleViewSet
from private.views import GroupViewSet, PrivateSubjectViewSet, PrivateViewSet
from student_projects.views import DailyPlanViewSet, ProjectViewSet, TeamViewSet
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
router.register(r'class-reports', ClassReportViewSet, basename='class-report')
router.register(r'non-teacher-reports', NonTeacherReportViewSet, basename='non-teacher-report')
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
router.register(r'extracurriculars', ExtracurricularViewSet, basename='extracurricular')
router.register(r'extracurricular-reports', ReportViewSet, basename='extracurricular-report')
router.register(r'extracurricular-scores', ScoreViewSet, basename='extracurricular-score')
router.register(r'private', PrivateViewSet, basename='private-lessons')
router.register(r'olympiad-fields', OlympiadFieldViewSet, basename='olympiad-field')
router.register(r'olympiad-reports', OlympiadReportViewSet, basename='olympiad-report')
router.register(r'private-subjects', PrivateSubjectViewSet, basename='private-subjects')
router.register(r'periods', PeriodViewSet, basename='period')
router.register(r'schedules', ScheduleViewSet, basename='schedule')
router.register(r'reporter-schedules', ReporterScheduleViewSet, basename='reporter-schedule')
router.register(r'private-groups', GroupViewSet, basename='private-groups')
router.register(r'blog-test', BlogTestViewSet, basename='blog-test')
router.register(r'category-test', CaterogytestViewSet, basename='category-test')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'student-project-teams', TeamViewSet, basename='student-project-team')
router.register(r'student-projects', ProjectViewSet, basename='student-project')
router.register(r'student-project-daily-plans', DailyPlanViewSet, basename='student-project-daily-plan')
router.register(r'lpj', LaporanPertanggungJawabanViewSet, basename='lpj')
router.register(r'proker', ProgramKerjaViewSet, basename='proker')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('api/v1/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/exchange-token/', exchange_token, name='token_exchange'),    
    path('api/v1/tahfidz-app/', include('tahfidz.urls')),
    path('api/v1/my-class-reports/quick-grid/generate/', generate_report_by_date, name='generate_report_for_current_date'),
    path('api/v1/my-class-reports/quick-grid/set-reporter/', set_current_reporter, name='generate_report_for_current_reporter'),
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