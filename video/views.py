from django.shortcuts import render, redirect
from .form import VideoForm
from django.shortcuts import get_object_or_404
from .models import Users
from django.contrib import messages
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        user= get_object_or_404(Users,user=request.user)
        if user.user_options == "Teacher":
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                video = form.save(commit=False)
                video.uploaded_by = user
                video.save()
                messages.success(request,'your data has been saved')
            return redirect('upload_video')
        else:
            form = VideoForm()
            messages.error(request,'You are not alowed to supmit video')
            return render(request, 'pages/upload_video.html', {'form': form})
    else:
        form = VideoForm()
    return render(request, 'pages/upload_video.html', {'form': form})


def videos(request):
    if request.user is not None :
        context=None
        if not request.user.is_anonymous:
            user= get_object_or_404(Users,user=request.user)
            videos = Video.objects.filter(uploaded_by=user)
            context={
                'videos': videos
            }
        return render(request,'pages/videos.html',context)
    else:
        return redirect('videos')
    
def videosuser(request,id):
    if request.user is not None :
        context=None
        if not request.user.is_anonymous:
            user = get_object_or_404(Users, user_id=id)
            videos = Video.objects.filter(uploaded_by=user)
            context={
                'videos': videos
            }
        return render(request,'pages/videos.html',context)
    else:
        return redirect('videos')
    
def video(request,id):
    if request.user is not None :
        context=None
        if not request.user.is_anonymous:
            video = get_object_or_404(Video, id=id)
            user = get_object_or_404(Users, user=video.uploaded_by.user)
            context={
                'video': video,
                'user':user
            }
        return render(request,'pages/video.html',context)
    else:
        return redirect('video')
    
def deletevideo(request,id):
    if request.user.is_authenticated:
        user= get_object_or_404(Users,user=request.user)
        video = Video.objects.filter(uploaded_by=user,id=id)
        if video:
           video.delete()
    return redirect('videos')