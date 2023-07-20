from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Video, Group , Users
from .forms import GroupForm
from django.shortcuts import get_object_or_404


@login_required
def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    user = get_object_or_404(Users, user=group.user.user)
    return render(request, 'pages/group_detail.html', {'group': group,'user':user})

@login_required
def group_create(request):
    user = get_object_or_404(Users, user=request.user)
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES,filter_video=user)
        if form.is_valid():
            group = form.save(commit=False)
            group.user = user
            group.save()
            form.save_m2m()  # Save the many-to-many relationships for the videos field
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm(filter_video=user)
    return render(request, 'pages/group_form.html', {'form': form})


@login_required
def group_edit(request, pk):
    group = Group.objects.get(pk=pk)
    user= get_object_or_404(Users,user=request.user)
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES, instance=group, filter_video=user)
        if form.is_valid():
            group = form.save(commit=False)
            group.user = user
            group.save()
            form.save_m2m()
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm(instance=group, filter_video=user)
    return render(request, 'pages/group_form.html', {'form': form})


@login_required
def group_delete(request, pk):
    if request.user.is_authenticated:
        group = get_object_or_404(Group, pk=pk)
        if request.method == 'POST':
            group.delete()
            return redirect('videos')
        
    return redirect('videos')
