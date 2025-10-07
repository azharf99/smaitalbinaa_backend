from rest_framework import viewsets, permissions
from utils.pagination import StandardResultsSetPagination
from utils.permissions import HasModelPermission
from .models import DailyPlan, Project, Team
from .serializers import DailyPlanSerializer, ProjectSerializer, TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all().order_by('-created_at')
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows student projects to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('-start_date', 'project_name')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

class DailyPlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows daily project plans to be viewed or edited.
    """
    queryset = DailyPlan.objects.all().order_by('-date')
    serializer_class = DailyPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

