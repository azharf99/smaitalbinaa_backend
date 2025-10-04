from rest_framework import serializers
from students.models import Student
from teachers.models import Teacher
from .models import DailyPlan, Project, Team


class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name']


class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name']


class TeamSerializer(serializers.ModelSerializer):
    team_leader = StudentNameSerializer(read_only=True)
    team_leader_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='team_leader', write_only=True
    )
    members = StudentNameSerializer(many=True, read_only=True)
    member_ids = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='members', write_only=True, many=True
    )

    class Meta:
        model = Team
        fields = [
            'id', 'team_leader', 'team_leader_id', 'members', 'member_ids',
            'prev_members', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']


class ProjectSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), source='team', write_only=True
    )
    teacher = TeacherNameSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True, allow_null=True
    )

    class Meta:
        model = Project
        fields = [
            'id', 'project_name', 'start_date', 'end_date', 'team', 'team_id',
            'teacher', 'teacher_id', 'description', 'step_to_achieve',
            'task_organizing', 'slug', 'semester', 'academic_year',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']


class DailyPlanSerializer(serializers.ModelSerializer):
    project = ProjectNameSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(), source='project', write_only=True
    )

    class Meta:
        model = DailyPlan
        fields = [
            'id', 'date', 'project', 'project_id', 'to_do_list', 'target_today',
            'problems', 'semester', 'academic_year', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']