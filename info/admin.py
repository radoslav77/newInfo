from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.base import Model
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password")


class Dish_RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'outlet', 'title', 'type_dish')


admin.site.register(Dish_Recipe, Dish_RecipeAdmin)


class BeverageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'alcochol_type')


admin.site.register(Beverage, BeverageAdmin)


class SharedRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'dish_title', 'type_dish')


admin.site.register(SharedRecipe, SharedRecipeAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'starter', 'main', 'dessert', 'drink')


admin.site.register(Menu, MenuAdmin)


class PairingAdmin(admin.ModelAdmin):
    list_display = ('dish', 'drink')


admin.site.register(Pairing, PairingAdmin)
