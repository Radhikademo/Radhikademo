from .models import User, Upload
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
class RegisterSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(RegisterSerializer, self).create(validated_data)

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = "__all__"

class UserLoginSerializer(serializers.Serializer):
    username = serializers.EmailField(max_length=255)
    password = serializers.CharField(
        max_length=128, write_only=True, style={"input_type": "password"}
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        fields = ['username', 'password', 'token']