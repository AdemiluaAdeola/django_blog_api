from django.shortcuts import render
from rest_framework import generics, permissions, pagination, status
from rest_framework.response import Response
from rest_framework.views import APIView
from blog_app.models import *
from blog_app.serializers import *

# Create your views here.
class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class BlogCategoryView(APIView):
    def get(self, request, format=None, **kwargs):
        blog = Blog.objects.filter(category__id = kwargs["id"])
        serializer = BlogListSerializer(instance=blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    permission_classes = [permissions.AllowAny]

class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = AddBlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogDetailView(APIView):
    def get(self, request, format=None, **kwargs):
        blog = Blog.objects.filter(id = kwargs["id"]).first()
        serializer = BlogPostSerializer(instance=blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AddCommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]