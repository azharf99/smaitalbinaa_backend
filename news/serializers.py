from rest_framework import serializers
from teachers.models import Teacher
from .models import Category, Post, Comment
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializer for the Teacher model, with nested user information.
    """
    class Meta:
        model = Teacher
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    author = TeacherSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'



class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    """
    Serializer for the Post model.
    Includes nested serializers for author and categories, and handles tags.
    """
    author = TeacherSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), 
        source="author", 
        write_only=True,
    )

    category = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        many=True, 
        source="category", 
        write_only=True,
    )

    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = '__all__'