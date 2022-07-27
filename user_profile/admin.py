from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user',"bio"]
    
class UserPostAdmin(admin.ModelAdmin):
    list_display=['user','post_text','created_at','update_at']

class FriendsAdmin(admin.ModelAdmin):
    list_display=['follow','following']

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserPost,UserPostAdmin)
admin.site.register(Friends,FriendsAdmin)