# Generated by Django 4.0.3 on 2022-03-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qrcode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genaratecode',
            name='outlet',
            field=models.CharField(choices=[('Room Service', 'Room Service'), ('Thoe', 'Thoe Randal'), ('Arch Bar', 'Arch Bar'), ('Wellington Lounge', 'Wellington Lounge'), ('Number One', 'Number One'), ('BQT', 'BQT'), ('Amenities', 'Amenities')], max_length=200),
        ),
    ]
