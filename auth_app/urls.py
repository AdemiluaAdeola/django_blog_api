from django.urls import path
from auth_app.views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='update_profile'),
    # path('profile/', UserProfileView.as_view(), name="profile"),
    path('userlist/', UserListView.as_view(), name="userlist"),
    path('profile/create/', ProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
]
