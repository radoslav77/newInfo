# Generated by Django 4.0.3 on 2022-03-24 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish_recipe',
            name='outlet',
            field=models.CharField(choices=[('Room Service', 'Room Service'), ('Thoe', 'Thoe Randal'), ('Arch Bar', 'Arch Bar'), ('Wellington Lounge', 'Wellington Lounge'), ('Number One', 'Number One'), ('BQT', 'BQT'), ('Amenities', 'Amenities')], max_length=200),
        ),
        migrations.AlterField(
            model_name='dish_recipe',
            name='sub_recipe',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='info.sharedrecipe'),
        ),
        migrations.AlterField(
            model_name='dish_recipe',
            name='type_dish',
            field=models.CharField(choices=[('Starter', 'Starter'), ('Main', 'Main'), ('Dessert', 'Dessert'), ('Amenities', 'Amenities')], max_length=200),
        ),
        migrations.AlterField(
            model_name='sharedrecipe',
            name='type_dish',
            field=models.CharField(choices=[('Starter', 'Starter'), ('Main', 'Main'), ('Dessert', 'Dessert'), ('Amenities', 'Amenities')], max_length=200),
        ),
    ]