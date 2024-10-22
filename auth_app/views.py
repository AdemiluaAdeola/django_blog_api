from rest_framework import permissions
from auth_app.serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.models import User
from rest_framework import generics, status
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

class ChangePasswordView(generics.RetrieveUpdateAPIView):

    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer

class UpdateProfileView(generics.RetrieveUpdateAPIView):

    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateUserSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class UserProfileView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if user.is_authenticated:
            return qs.filter(username = user.username)
        else:
            return User.objects.none()

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer

class ProfileCreateView(generics.CreateAPIView):
    """
    View to create a new profile.
    - Only authenticated users can create a profile.
    - Admins can see all profiles.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user as the profile owner
        serializer.save(user=self.request.user)

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, pk, format=None):
        profile = get_object_or_404(Profile, user__id=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        profile = get_object_or_404(Profile, user__id=pk)
        
        # Ensure the user can only update their own profile
        if request.user.id != profile.user.id:
            return Response({"detail": "Not authorized to update this profile."}, status=status.HTTP_403_FORBIDDEN)
        
        else:
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
