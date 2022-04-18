from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.base import Model
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password")


class Dish_RecipeAdmin(admin.ModelAdmin):
    list_display = ('id',  'title', 'date')


admin.site.register(Dish_Recipe, Dish_RecipeAdmin)


class BeverageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand')


admin.site.register(Beverage, BeverageAdmin)


class SharedRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'dish_title')


admin.site.register(SharedRecipe, SharedRecipeAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')


admin.site.register(Menu, MenuAdmin)


class PairingAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Pairing, PairingAdmin)


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Dish, DishAdmin)


class CaloryAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'calory')


admin.site.register(Calory, CaloryAdmin)


class WightsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'wight')


admin.site.register(Wights, WightsAdmin)
