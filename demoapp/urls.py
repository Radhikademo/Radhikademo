from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)
from .views import (RegisterView,
                    LoginView,
                    UploadAPIView,
                    UserDetailView,
                    UserDeleteView,
                    PostDetailView,
                    PostDeleteView)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('upload/', UploadAPIView.as_view(), name='upload'),
    path('user-details/<int:pk>/', UserDetailView.as_view(), name = 'user-details'),
    path('delete_user/', UserDeleteView.as_view(), name='delete_user'),
    path('post_detail/', PostDetailView.as_view(), name='post_detail'),
    path('post_delete/', UserDeleteView.as_view(), name='post_delete')
    ]
