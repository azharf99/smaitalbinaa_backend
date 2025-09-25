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
    # For read operations (GET), display the full nested user object.
    user = UserSerializer(read_only=True)

    # For write operations (POST, PUT), accept a user ID.
    # This field will not be shown in the API output.
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )

    class Meta:
        model = Teacher
        # Explicitly list fields to include our new 'user_id' for write operations.
        fields = ['id', 'user', 'user_id', 'niy', 'teacher_name', 'short_name', 'gender', 'address', 'job', 'email', 'phone', 'photo', 'work_area', 'status', 'day_off', 'created_at', 'updated_at']