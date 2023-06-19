from django.shortcuts import render, redirect
from .form import VideoForm
from django.shortcuts import get_object_or_404
from .models import Users

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            user= get_object_or_404(Users,user=request.user)
            video.uploaded_by = user
            video.save()
            return redirect('index')
    else:
        form = VideoForm()
    return render(request, 'pages/upload_video.html', {'form': form})