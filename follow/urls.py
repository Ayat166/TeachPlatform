from django.urls import path 
from . import views
urlpatterns = [
    path('<int:id>/',views.follow,name='follow'),
    path('unfollow/<int:id>/',views.unfollow,name='unfollow'),
]
