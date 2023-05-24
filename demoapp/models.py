from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    user_Name = models.EmailField(max_length=250,unique=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    email_verified = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True, auto_now_add=True)
class Meta:
    # managed = False    
    db_table = 'user'


class Upload(models.Model):
    '''upload file'''
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, )
    files = models.FileField(upload_to="my_uploads/", max_length=500, null=True, blank=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        # managed = False    
        db_table = 'upload'
