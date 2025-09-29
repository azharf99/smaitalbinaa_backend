from rest_framework import serializers
from students.models import Student
from teachers.models import Teacher
from .models import OlympiadField, OlympiadReport


class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name']


class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name']


class OlympiadFieldNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = OlympiadField
        fields = ['id', 'field_name', 'type']


class OlympiadFieldSerializer(serializers.ModelSerializer):
    teacher = TeacherNameSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True, allow_null=True
    )
    members = StudentNameSerializer(many=True, read_only=True)
    member_ids = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='members', write_only=True, many=True
    )

    class Meta:
        model = OlympiadField
        fields = [
            'id', 'field_name', 'teacher', 'teacher_id', 'schedule',
            'members', 'member_ids', 'type', 'slug', 'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']


class OlympiadReportSerializer(serializers.ModelSerializer):
    field_name = OlympiadFieldNameSerializer(read_only=True)
    field_name_id = serializers.PrimaryKeyRelatedField(
        queryset=OlympiadField.objects.all(), source='field_name', write_only=True
    )
    students = StudentNameSerializer(many=True, read_only=True)
    student_ids = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='students', write_only=True, many=True
    )

    class Meta:
        model = OlympiadReport
        fields = [
            'id', 'field_name', 'field_name_id', 'report_date', 'students',
            'student_ids', 'report_photo', 'notes', 'semester',
            'academic_year', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']