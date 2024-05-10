from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_sheet, name='character_sheet'),
    #path('sheet/<id>/', views.sheet_detail, name='sheet_detail'), #doesn't do anything yet; need sheet_detail view and html template
    path('sheet/new/', views.character_sheet_new, name='sheet_new')
]