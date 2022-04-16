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


class SharedRecipeForm(forms.ModelForm):

    class Meta:
        model = SharedRecipe

        fields = ('title', 'dish_title',
                  'type_dish', 'recipe', 'method')


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Dish_Recipe
        fields = '__all__'
    # remove requarments of the field

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, *kwargs)
        self.fields['dish_title'].required = False


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, *kwargs)
        self.fields['recipe'].required = False


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('title', 'starters', 'main', 'dessert', 'drink')

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, *kwargs)
        self.fields['drink'].required = False


class BeverageForm(forms.ModelForm):

    class Meta:
        model = Beverage
        fields = ('title', 'alcohol_type', 'description', 'brand', 'alergens')


class PairingForm(forms.ModelForm):

    class Meta:
        model = Pairing
        fields = ('dish_title', 'bev_title')


class CaloryForm(forms.ModelForm):
    class Meta:
        model = Calory
        fields = '__all__'
