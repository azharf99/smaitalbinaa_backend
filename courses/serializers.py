from rest_framework import serializers
from .models import Course, Subject
from teachers.models import Teacher
from classes.models import Class


class TeacherNameSerializer(serializers.ModelSerializer):
    """
    A simple serializer to represent a Teacher by name.
    """
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name']


class ClassNameSerializer(serializers.ModelSerializer):
    """
    A simple serializer to represent a Class by its short name.
    """
    class Meta:
        model = Class
        fields = ['id', 'short_class_name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    course = SubjectSerializer(read_only=True)
    teacher = TeacherNameSerializer(read_only=True)
    class_assigned = ClassNameSerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'course', 'course_code', 'teacher', 'type', 'class_assigned',
            'periods_per_week', 'consecutive_periods_needed', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']