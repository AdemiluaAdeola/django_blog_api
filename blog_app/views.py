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

class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BlogListSerializer
        
        elif self.request.method == 'POST':
            return AddBlogPostSerializer
        
    def perform_create(self, serializer):
        # Automatically set the author to the current logged-in user
        serializer.save(author=self.request.user)

# class BlogCreateView(generics.ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = AddBlogPostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         # Automatically set the author to the current logged-in user
#         serializer.save(author=self.request.user)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [IsAuthorOrAdmin]

class CommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None, *args, **kwargs):
        try:
            # Fetch the latest comment for the blog post
            comment = Comment.objects.filter(blog__id=kwargs['pk']).latest('created_at')
        except Comment.DoesNotExist:
            return Response({"detail": "No comments found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def post(self, request, format=None, *args, **kwargs):
        # Extract the blog post ID from the URL (kwargs['pk'])
        blog_id = kwargs['pk']

        # Add the blog ID to the comment data
        data = request.data.copy()
        data['blog'] = blog_id

        # Deserialize the incoming data
        serializer = CommentSerializer(data=data)

        # Validate and save the comment if the data is valid
        if serializer.is_valid():
            serializer.save(author=request.user)  # Assuming 'author' is a ForeignKey to the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)