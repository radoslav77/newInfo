from typing import ChainMap
from unicodedata import name
from django.urls import path
from . import views

app_name = "info"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login_user'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logout_user'),
    path('password-change/<str:user>',
         views.change_password, name='change_password'),
    path('input_dish', views.input_dish, name='input_dish'),
    path('input_subrecipe', views.input_subrecipe, name='input_subrecipe'),
    path('menu', views.menu, name='menu'),
    path('beveridge', views.beveridge, name='beveridge'),
    path('recipeInput', views.recipe_input, name='recipe_input'),
    path('calory-input', views.calory_input, name='calory_input'),
    path('wight-input', views.wight_input, name='wight_input'),
    path('dishes', views.dishes, name='dishes'),
    path('detail/<str:title>', views.detail, name='detail'),


    # API
    path('calory_data', views.calory_data, name='calory_data'),
    path('wight_data', views.wight_data, name='wight_data'),
    path('recipe_data', views.recipe_data, name='recipe_data'),
    # path('subrecipe_data', views.subrecipe_data, name='subrecipe_data')

]
