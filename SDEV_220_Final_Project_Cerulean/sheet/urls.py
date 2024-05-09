from django.urls import path
from . import views

urlpatterns = [
    path('sheet/new/', views.character_sheet, name='character_sheet'), #I'm only including one url for now because I'm mostly concerned about players being able to create a sheet
]