# Generated by Django 4.0.3 on 2022-04-17 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_rename_recipe_dish_choose_recipe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='choose_recipe',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='choose_subrecipe',
        ),
    ]
