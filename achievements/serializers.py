from rest_framework import serializers
from students.models import Student
from .models import Prestasi, ProgramPrestasi

class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name']

class PrestasiSerializer(serializers.ModelSerializer):
    """
    Serializer for the Prestasi model.
    """
    student_details = StudentNameSerializer(source='student', read_only=True)
    class Meta:
        model = Prestasi
        fields = '__all__'
        extra_kwargs = {
            'student': {'write_only': True, 'required': False, 'allow_null': True}
        }


class ProgramPrestasiSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProgramPrestasi model.
    """
    class Meta:
        model = ProgramPrestasi
        fields = '__all__'