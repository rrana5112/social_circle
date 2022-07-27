from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

from user_profile.models import Friends, UserProfile

# Create your views here.

def home(request):
    return render(request,'index.html')

def login_view(request):
    if request.method=='GET':
      return render(request,'login.html')
    if request.method=='POST':
        data=request.POST
        password = data.get('password')
        username = data.get('username')
        x = User.objects.filter(username=username).first()
        print(x)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/user-profile') 
        else:
            return redirect('login') 

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        data=request.POST
        request_data = dict(first_name = data.get('first_name'),
        last_name = data.get('last_name'),
        email = data.get('email'),
        password = make_password(data.get('password')),
        username = data.get('username'))

        user = User.objects.create(**request_data)
        return redirect('home')


def user_profile(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if profile:
        profile = profile.__dict__
        if profile.get('image'):
            profile['image'] = settings.MEDIA_URL+profile['image']
    else:
        profile={}
    return render(request,'user-timeline.html',context=profile)

def friend_list(request):
    if request.method=='GET':
        friends_data=[]
        friends = Friends.objects.filter(follow=request.user)
        for friend in friends:
            friends_data.append({"username":friend.following.username,"first_name":friend.following.first_name,"last_name":friend.following.last_name,"post":1,"comments":10,"views":0})
        return render(request,'user-friends.html',context={"friends_list":friends_data})