from django.shortcuts import render

# Create your views here.

from .models import Users

def index(request):
    users=Users.objects.all()
    return render(request,"index.html",{"users":users})