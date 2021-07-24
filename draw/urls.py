# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('small/', views.small, name='small'),
    path('big/', views.big, name='big'),
    path('<str:room_name>/', views.room, name='room'),

]
