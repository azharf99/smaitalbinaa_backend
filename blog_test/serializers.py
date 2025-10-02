from rest_framework import serializers
from teachers.models import Teacher
from .models import BlogTest, Caterogytest
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from taggit.models import Tag


class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializer for the Teacher model, with nested user information.
    """
    class Meta:
        model = Teacher
        fields = '__all__'


class CaterogytestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caterogytest
        fields = '__all__'



class BlogTestSerializer(TaggitSerializer, serializers.ModelSerializer):
    """
    Serializer for the BlogTest model.
    Includes nested serializers for author and categories, and handles tags.
    """

    author = TeacherSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), 
        source="author", 
        write_only=True,
    )
    category = serializers.StringRelatedField(many=True, read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Caterogytest.objects.all(), 
        source="category", 
        write_only=True,
        many=True,
    )


    class Meta:
        model = BlogTest
        fields = '__all__'