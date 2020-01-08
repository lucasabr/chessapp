from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chess-home'),
    path('', views.home, name='chess-home')
]