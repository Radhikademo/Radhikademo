from django.contrib import admin
from django.urls import path, include
from .views import (RegisterView,
                    UploadAPIView,
                    UserDetailView,
                    UserDeleteView,
                    PostDetailView,
                    PostDeleteView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('upload/', UploadAPIView.as_view(), name='upload'),
    path('user-details/<int:pk>/', UserDetailView.as_view(), name = 'user-details'),
    path('delete_user/', UserDeleteView.as_view(), name='delete_user'),
    path('post_detail/', PostDetailView.as_view(), name='post_detail'),
    path('post_delete/', UserDeleteView.as_view(), name='post_delete')
    ]
