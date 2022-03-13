from distutils.command.upload import upload
from pyexpat import model
from tkinter import CASCADE
from turtle import title
from django.db import models

# Create your models here.

COURSE = [
    ('Starter', 'Starter'),
    ('Main', 'Main'),
    ('Dessert', 'Dessert'),
]


class Dish_Recipe(models.Model):
    OUTLET = [
        ('Room Service', 'Room Service'),
        ('Thoe', 'Thoe Randal'),
        ('Arch Bar', 'Arch Bar'),
        ('Wellington Lounge', 'Wellington Lounge'),
        ('Number One', 'Number One'),
        ('BQT', 'BQT')
    ]

    title = models.CharField(max_length=200)
    outlet = models.CharField(max_length=200, choices=OUTLET)
    type_dish = models.CharField(choices=COURSE)
    recipe = models.TextField(max_length=4000)
    method = models.TextField(max_length=6000)
    sub_recipe = models.ForeignKey('SharedRecipe', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='media')
    archived = models.BooleanField(default=False)
    shared = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class SharedRecipe(models.Model):
    title = models.CharField(max_length=200)
    dish_title = models.ForeignKey(Dish_Recipe, on_delete=models.CASCADE)
    type_dish = models.CharField(choices=COURSE)
    recipe = models.TextField(max_length=4000)
    method = models.TextField(max_length=6000)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title, self.dish_title}'

    class Meta:
        ordering = ('title', )


class Beverage(models.Model):
    TYPE = [
        ('Soft', 'Soft'),
        ('Coffee', 'Coffee'),
        ('Tea', 'Tea'),
        ('Juice', 'Juice'),
        ('Beer', 'Beer'),
        ('Wine', 'Wine'),
        ('Sparkling Wine', 'Sparkling Wine'),
        ('Spirit', 'Spirit'),
        ('Shot', 'Shot')
    ]
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=400)
    description = models.TextField(max_length=4000)
    alcohol_type = models.CharField(max_length=200, choices=TYPE)
    alergens = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )


class Pairing(models.Model):
    dish_title = models.ForeignKey(Dish_Recipe, on_delete=models.CASCADE)
    bev_title = models.ForeignKey(Beverage, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.id


class Menu(models.Model):
    title = models.CharField(max_length=200)
    starters = models.ForeignKey(Dish_Recipe, on_delete=models.CASCADE)
    main = models.ForeignKey(Dish_Recipe, on_delete=models.CASCADE)
    dessert = models.ForeignKey(Dish_Recipe, on_delete=models.CASCADE)
    drink = models.ForeignKey(Beverage, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
