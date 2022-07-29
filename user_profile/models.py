

from datetime import timedelta
from itertools import count
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

    @property
    def created_at_ist(self):
        return self.created_at+timedelta(hours=5.5)
    
    @property
    def reactions(self):
        return PostReaction.objects.filter(post=self).count()
    
    @property
    def comments(self):
        return PostComment.objects.filter(post=self).count()
    


class Friends(models.Model):
    follow=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='follow')
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')

    


class PostComment(models.Model):
    post=models.ForeignKey(UserPost,on_delete=models.CASCADE,related_name='post_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_by')
    comment=models.TextField(null=True,blank=True)

reaction_choice = (
        ('Like','Like'),
        ('Laugh', 'Laugh'),
        ('Wow','Wow'),
        ('love','love'),
    )


class PostReaction(models.Model):
    post=models.ForeignKey(UserPost,on_delete=models.CASCADE,related_name='post_reaction')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reaction_by')
    reaction=models.TextField(choices=reaction_choice,null=True,blank=True)



class BlockedUser(models.Model):
    blocked_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blocked')
    blocked_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blocked_by')