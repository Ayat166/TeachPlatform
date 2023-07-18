from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Video, Group , Users
from .forms import GroupForm
from django.shortcuts import get_object_or_404

@login_required
def group_list(request):
    user= get_object_or_404(Users,user=request.user)
    groups = Group.objects.filter(user=user)
    return render(request, 'pages/videos.html', {'groups': groups})

@login_required
def group_detail(request, pk):
    group = Group.objects.get(pk=pk)
    return render(request, 'pages/group_detail.html', {'group': group})

@login_required
def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            user= get_object_or_404(Users,user=request.user)
            group = form.save(commit=False)
            group.user = user
            group.save()
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm()
    return render(request, 'pages/group_form.html', {'form': form})

@login_required
def group_edit(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            user= get_object_or_404(Users,user=request.user)
            group.user = user
            group.save()
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm(instance=group)
    return render(request, 'pages/group_form.html', {'form': form})
