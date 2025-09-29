from rest_framework import serializers
from students.models import Student
from extracurriculars.models import Extracurricular
from .models import Score


class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name']


class ExtracurricularNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extracurricular
        fields = ['id', 'name']


class ScoreSerializer(serializers.ModelSerializer):
    student = StudentNameSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student', write_only=True
    )
    extracurricular = ExtracurricularNameSerializer(read_only=True)
    extracurricular_id = serializers.PrimaryKeyRelatedField(
        queryset=Extracurricular.objects.all(), source='extracurricular', write_only=True
    )

    class Meta:
        model = Score
        fields = [
            'id', 'student', 'student_id', 'extracurricular', 'extracurricular_id',
            'score', 'semester', 'academic_year', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']