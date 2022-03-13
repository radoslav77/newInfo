from django.db import models


# Create your models here.
OUTLET = [
    ('Room Service', 'Room Service'),
    ('Thoe', 'Thoe Randal'),
    ('Arch Bar', 'Arch Bar'),
    ('Wellington Lounge', 'Wellington Lounge'),
    ('Number One', 'Number One'),
    ('BQT', 'BQT')
]


class GenarateCode(models.Model):
    title = models.CharField(max_length=200)
    outlet = models.CharField(max_length=200, choices=OUTLET)
