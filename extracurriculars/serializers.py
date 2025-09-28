from rest_framework import serializers

from students.models import Student
from teachers.models import Teacher
from .models import Extracurricular

class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name']

class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name']

class ExtracurricularSerializer(serializers.ModelSerializer):
    teacher_details = TeacherNameSerializer(source='teacher', many=True, read_only=True)
    member_details = StudentNameSerializer(source='members', many=True, read_only=True)

    class Meta:
        model = Extracurricular
        fields = '__all__'