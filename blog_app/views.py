from django.shortcuts import render
from rest_framework import generics, permissions, pagination, status
from rest_framework.response import Response
from rest_framework.views import APIView
from blog_app.models import *
from blog_app.serializers import *
from blog_app.permission import IsAuthorOrAdmin

# Create your views here.
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogCreateView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = AddBlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [IsAuthorOrAdmin]

