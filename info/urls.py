from typing import ChainMap
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login_user'),
    path('register', views.register, name='register'),
    path('password-change/<str:user>',
         views.change_password, name='change_password'),
]
