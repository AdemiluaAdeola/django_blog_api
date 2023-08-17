from rest_framework import serializers
from blog_app.models import *

#category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]

class AddBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "author",
            "category",
            "snippet",
            "body",
        ]

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "author",
            "created_at",
            "snippet",
        ]

class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "name",
            "created_at",
            "body",
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    comments = AddCommentSerializer(read_only=True, many=True)
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "author",
            "created_at",
            "category",
            "body",
            "comments",
        ]
