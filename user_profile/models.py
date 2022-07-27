
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile')
    bio=models.TextField(blank =True,null=True)
    image=models.ImageField(upload_to='profiles',blank=True,null =True)
    country=models.CharField(max_length=25,blank=True,null =True)
    address=models.TextField(blank=True,null =True)
    website=models.URLField(blank=True,null =True)

class UserPost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userpost')
    post_text=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='post',blank=True,null =True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

class Friends(models.Model):
    follow=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow')
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')