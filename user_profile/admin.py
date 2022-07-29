
from django.contrib import admin

from user_profile.views import register
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user',"bio"]
    
class UserPostAdmin(admin.ModelAdmin):
    list_display=['user','post_text','created_at','update_at']

class FriendsAdmin(admin.ModelAdmin):
    list_display=['follow','following']

class PostReactionAdmin(admin.ModelAdmin):
    list_display=['post','user','reaction']
    list_filter=['reaction']

class PostCommentAdmin(admin.ModelAdmin):
    list_display=['post','user','comment']
    

class BlockedUserAdmin(admin.ModelAdmin):
    list_display=['blocked_user','blocked_by']

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserPost,UserPostAdmin)
admin.site.register(Friends,FriendsAdmin)
admin.site.register(PostReaction,PostReactionAdmin)
admin.site.register(PostComment,PostCommentAdmin)
admin.site.register(BlockedUser,BlockedUserAdmin)
