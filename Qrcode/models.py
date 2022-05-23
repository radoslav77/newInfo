from pyexpat import model
from django.db import models


# Create your models here.
OUTLET = [
    ('Room Service', 'Room Service'),
    ('Thoe', 'Thoe Randal'),
    ('Arch Bar', 'Arch Bar'),
    ('Wellington Lounge', 'Wellington Lounge'),
    ('Number One', 'Number One'),
    ('BQT', 'BQT'),
    ('Amenities', 'Amenities')
]


class GenarateCode(models.Model):
    title = models.CharField(max_length=200)
    outlet = models.CharField(max_length=200, choices=OUTLET)
    img = models.ImageField(upload_to='media')
    date = models.DateField(auto_now_add=True, null=True)


class QRcodesForDishes(models.Model):
    title = models.CharField(max_length=200)
    outlet = models.CharField(max_length=200, default='q')
    img = models.ImageField(upload_to='media')
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
