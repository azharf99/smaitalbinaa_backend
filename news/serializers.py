from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

from teachers.models import Teacher
from teachers.serializers import TeacherSerializer  # Assuming you have this serializer
from .models import Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']
        read_only_fields = ['slug']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'body', 'created_at', 'active']
        read_only_fields = ['author', 'created_at', 'active']


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
    # author = serializers.StringRelatedField(read_only=True)
    # category = serializers.StringRelatedField(read_only=True, many=True)

    category = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        many=True, 
        source="category", 
        write_only=True,
    )

    tags = TagListSerializerField()

    comments = CommentSerializer(many=True, read_only=True)



    class Meta:
        model = Post
        fields = [
            "id", "title", "slug", "content", "author", "author_id",
            "category", "category_ids", "tags", "status", "featured_image",
            "created_at", "updated_at", "comments",
        ]
        read_only_fields = ["slug", "created_at", "updated_at"]

    class Meta:
        model = Post
        fields = '__all__'