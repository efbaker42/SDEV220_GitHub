from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_sheet, name='character_sheet'),
    #path('sheet/list', views.sheet_list, name='sheet_list'),
    path('sheet/<pk>/', views.sheet_detail, name='sheet_detail'), #doesn't do anything yet; need sheet_detail view and html template
    path('sheet/new/', views.character_sheet_new, name='new_sheet'), #name is the name of the url; may be referenced elsewhere
    path('sheet/new/sheet_detail/', views.sheet_detail, name='new_sheet_detail'), #should display just-made sheet
    path('sheet/error_message/', views.error_message, name='error_message'),
    path('sheet/success_message/', views.success_message, name='success_message'),
]