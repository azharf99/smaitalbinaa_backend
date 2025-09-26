from rest_framework import serializers
from .models import Student
from classes.models import Class
from classes.serializers import ClassSerializer

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Student model, with nested class information.
    """
    # For read operations (GET), display the full nested class object.
    student_class = ClassSerializer(read_only=True) # For GET requests

    # For write operations (POST, PUT), accept a class ID.
    student_class_id = serializers.PrimaryKeyRelatedField( # For POST/PUT requests
        queryset=Class.objects.all(),
        source='student_class',
        write_only=True,
        allow_null=True, # Allow students to not be in a class
        required=False
    )

    class Meta:
        model = Student
        # Explicitly list all fields for better security and clarity.
        # 'student_class' is for reading, 'student_class_id' is for writing.
        fields = ['id', 'nis', 'nisn', 'student_name', 'gender', 'student_birth_place', 'student_birth_date', 'student_status', 'photo', 'student_class', 'student_class_id', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']