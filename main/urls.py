from django.urls import path, include 
from . import views
from django.contrib.auth import views as auth_views
from register import views

urlpatterns = [ 
    path('', views.home , name="site-home"),
    path('chess/', include('chess.urls') ),
    path('ttt/', include('ttt.urls')),
    path('register/', include('register.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="login/home.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="login/logout.html"), name='logout'),
    path('profile/', views.profile, name='user-profile')

]