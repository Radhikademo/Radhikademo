from .models import User, Upload
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
class RegisterSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data['pwd'] = make_password(validated_data['pwd'])
        return super(RegisterSerializer, self).create(validated_data)

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ("First_Name", "Last_Name")