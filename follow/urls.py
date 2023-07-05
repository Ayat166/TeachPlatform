from django.urls import path 
from . import views
urlpatterns = [
    path('follow/<int:id>',views.follow,name='follow'),
]
