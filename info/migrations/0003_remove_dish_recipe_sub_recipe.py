# Generated by Django 4.0.3 on 2022-03-24 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_dish_recipe_outlet_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish_recipe',
            name='sub_recipe',
        ),
    ]
