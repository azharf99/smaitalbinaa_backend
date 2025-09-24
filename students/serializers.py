from rest_framework import serializers
from .models import Student
from classes.serializers import ClassSerializer

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Student model.
    """
    # Use the ClassSerializer to represent the student_class foreign key.
    # This will nest the full class object in the student's JSON representation.
    # The `read_only=True` flag means this nested data is for representation only
    # and won't be used for write operations directly on this serializer.
    student_class = ClassSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'