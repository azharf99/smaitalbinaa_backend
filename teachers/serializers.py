from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Teacher

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the built-in User model to show related user details.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializer for the Teacher model, with nested user information.
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'