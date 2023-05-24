from django.shortcuts import render
from rest_framework import generics, status
from .serializers import (RegisterSerializer,
                          UploadSerializer,
                          UserDetailsSerializer,
                          UserLoginSerializer)
from rest_framework.response import Response
from .models import User, Upload
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate


class RegisterView(generics.GenericAPIView):
    """
    user register api
    """
    serializer_class = RegisterSerializer
    def post(self, request):
        try:
            user = request.data
            serilizer = self.serializer_class(data=user, context={'request': request})
            if serilizer.is_valid():
                serilizer.save()
                return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        except:
            return Response(self.serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    """
    user login api
    """
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        breakpoint()
        data = request.data
        username = data.get("username", "")
        password = data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            serializer_class = UserLoginSerializer(data=request.data)
            if serializer_class.is_valid(raise_exception=True):
                if not user.is_active:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
                user_data = {"user_id": user.id, "email":user.username, "tokens":user.tokens}
                message = "login_success"
                return Response({'message':message, 'data':user_data}, status=status.HTTP_200_OK)
        return Response({'status':'login_invalid_credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserDetailView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailsSerializer
    def get(self, request, pk, format=None):
        try:
            data = get_object_or_404(User, pk=pk)
            if data:
                serializer = self.serializer_class(data)
                return Response(serializer.data)
            else:
                data = User.objects.all()
                serializer = self.serializer_class(data, many=True)
                return Response(serializer.data)
        except:
            message ="data_not_found"
            return Response(self.serializer_class.errors, status=status.HTTP_404_NOT_FOUND)

class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailsSerializer
    def delete(self, request):
        try:
            user = User.bjects.filter(id=request.data['id'])
            if user:
                user.delete()
                return Response({"status": True, 'message': "User deleted successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status": False, 'message': "User not found"}, status=status.HTTP_403_FORBIDDEN)
            
        except Exception as e:
            return Response({'massege':e.args}, status=status.HTTP_400_BAD_REQUEST)

class UploadAPIView(generics.GenericAPIView):   
    """
    user uploads
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UploadSerializer
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        except:
            return Response(self.serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailsSerializer
    def get(self, request, pk, format=None):
        try:
            data = get_object_or_404(Upload, pk=pk)
            if data:
                serializer = self.serializer_class(data)
                return Response(serializer.data)
            else:
                data = Upload.objects.all()
                serializer = self.serializer_class(data, many=True)
                return Response(serializer.data)
        except:
            message ="data_not_found"
            return Response(self.serializer_class.errors, status=status.HTTP_404_NOT_FOUND)

class PostDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailsSerializer
    def delete(self, request):
        try:
            user = Upload.bjects.filter(id=request.data['id'])
            if user:
                user.delete()
                return Response({"status": True, 'message': "User deleted successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status": False, 'message': "User not found"}, status=status.HTTP_403_FORBIDDEN)
            
        except Exception as e:
            return Response({'massege':e.args}, status=status.HTTP_400_BAD_REQUEST)