from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    path('upload_video',views.upload_video,name='upload_video'),
    path('videos',views.videos,name='videos'),
    path('videos/<int:id>',views.videosuser,name='videosuser'),
    path('<int:id>',views.video,name='video'),
]
