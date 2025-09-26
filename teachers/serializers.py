from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Teacher

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the built-in User model to show related user details.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'date_joined']

class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializer for the Teacher model, with nested user information.
    """
    # Use a nested serializer for read operations to show full user details.
    # For write operations, we expect a user ID. We also filter the queryset
    # to ensure only active staff members can be assigned as teachers.
    user = UserSerializer(read_only=True) # For GET requests
    user_id = serializers.PrimaryKeyRelatedField( # For POST/PUT requests
        queryset=User.objects.filter(is_staff=True, is_active=True),
        source='user',
        write_only=True
    )

    class Meta:
        model = Teacher
        # List all fields from the model, plus the write-only 'user_id'.
        # 'user' is included for read operations.
        fields = ['id', 'user', 'user_id', 'niy', 'teacher_name', 'short_name', 'gender', 'address', 'job', 'email', 'phone', 'photo', 'work_area', 'status', 'day_off', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def to_representation(self, instance):
        """Ensure the user object is fully serialized on read."""
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        return representation