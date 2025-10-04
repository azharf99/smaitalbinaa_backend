from rest_framework import viewsets
from utils.pagination import StandardResultsSetPagination
from .models import DailyPlan, Project, Team
from .serializers import DailyPlanSerializer, ProjectSerializer, TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all().order_by('-created_at')
    serializer_class = TeamSerializer
    pagination_class = StandardResultsSetPagination

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows student projects to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('-start_date', 'project_name')
    serializer_class = ProjectSerializer
    pagination_class = StandardResultsSetPagination

class DailyPlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows daily project plans to be viewed or edited.
    """
    queryset = DailyPlan.objects.all().order_by('-date')
    serializer_class = DailyPlanSerializer
    pagination_class = StandardResultsSetPagination

