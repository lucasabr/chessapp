from django.urls import path, include 
from . import views

urlpatterns = [ 
    path('', views.home , name="site-home"),
    path('chess/', include('chess.urls') ),
    path('ttt/', include('ttt.urls')),
    path('login/', include('login.urls'))
]