from typing import ChainMap
from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login_user'),
    path('register', views.register, name='register'),
    path('password-change/<str:user>',
         views.change_password, name='change_password'),
    path('input_dish', views.input_dish, name='input_dish'),
    path('input_subrecipe', views.input_subrecipe, name='input_subrecipe'),
    path('menu', views.menu, name='menu'),
    path('beveridge', views.beveridge, name='beveridge'),
    path('recipeInput', views.recipe_input, name='recipe_input'),

]
