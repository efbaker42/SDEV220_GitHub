from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_sheet, name='character_sheet'),
]