from django.shortcuts import render ,redirect
from .models import Follow ,Users
from django.shortcuts import get_object_or_404

# Create your views here.
def follow(requset,id):
    if requset.user.is_authenticated:
        followed = get_object_or_404(Users,user_id=id)
        follow = Follow.objects.create(following=requset.user.users,followed=followed)
    return redirect("index")

