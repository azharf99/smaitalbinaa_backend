from rest_framework import serializers

from news.serializers import TeacherSerializer
from teachers.models import Teacher
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    """Serializer for the Notification model."""
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), 
        source="teacher", 
        write_only=True,
    )
    
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ('teacher',)