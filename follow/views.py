from django.shortcuts import render ,redirect
from .models import Follow ,Users
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
def follow(request,id):
    if request.user.is_authenticated:
        followed = get_object_or_404(Users,user_id=id)
        if followed.user_options == "Teacher":
            if request.user != followed.user:
                follow = Follow.objects.filter(following=request.user.users,followed=followed)
                if not follow:
                    follow = Follow.objects.create(following=request.user.users,followed=followed)
                    follow.save()
                else:
                    messages.error( request,f"You already follow {followed.user.username}")
            else:
                messages.error( request,'You Cannot follow Youself')
        else:
           messages.error( request,'You Cannot follow Student')
    else:
        messages.error( request,'You Should Login')
    return redirect('profileuser', user_id=id)


def unfollow(request,id):
    if request.user.is_authenticated:
        followed = get_object_or_404(Users,user_id=id)
        follow = Follow.objects.filter(following=request.user.users,followed=followed)
        if follow:
           follow.delete()
    return redirect('profileuser', user_id=id)
