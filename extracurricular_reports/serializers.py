from rest_framework import serializers
from students.models import Student
from teachers.models import Teacher
from extracurriculars.models import Extracurricular
from .models import Report


class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name']


class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name']


class ExtracurricularNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extracurricular
        fields = ['id', 'name']


class ReportSerializer(serializers.ModelSerializer):
    extracurricular = ExtracurricularNameSerializer(read_only=True)
    extracurricular_id = serializers.PrimaryKeyRelatedField(
        queryset=Extracurricular.objects.all(), source='extracurricular', write_only=True
    )
    teacher = TeacherNameSerializer(many=True, read_only=True)
    teacher_ids = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True, many=True
    )
    students = StudentNameSerializer(many=True, read_only=True)
    student_ids = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='students', write_only=True, many=True
    )

    class Meta:
        model = Report
        fields = [
            'id', 'extracurricular', 'extracurricular_id', 'teacher', 'teacher_ids',
            'report_date', 'report_notes', 'students', 'student_ids', 'photo',
            'semester', 'academic_year', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']