from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    path('<int:pk>/', views.group_detail, name='group_detail'),
    path('create/', views.group_create, name='group_create'),
    path('<int:pk>/edit/', views.group_edit, name='group_edit'),
    path('<int:pk>/delete/', views.group_delete, name='group_delete'),
]
