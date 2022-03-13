from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.views.generic.edit import FormView

from .models import *


class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SharedRecipe(forms.ModelForm):

    class Meta:
        model = SharedRecipe

        fields = ('title', 'dish_title',
                  'type_dish', 'recipe', 'method')


class Dish_Recipe(forms.ModelForm):

    class Meta:
        model = Dish_Recipe
        fields = ('title', 'type_dish', 'outlet',
                  'recipe',  'method', 'sub_recipe', 'picture',)


class Menu(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('title', 'starters', 'main', 'dessert', 'drink')


class Beverage(forms.ModelForm):

    class Meta:
        model = Beverage
        fields = ('title', 'alcohol_type', 'description', 'brand', 'alergens')


class Pairing(forms.ModelForm):

    class Meta:
        model = Pairing
        fields = ('dish_title', 'bev_title')
