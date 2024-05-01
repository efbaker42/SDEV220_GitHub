from django.urls import path
from . import views #imports views from this file

urlpatterns = [
    path('', views.post_list, name='post_list'),
]