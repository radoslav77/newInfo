# Generated by Django 4.0.3 on 2022-03-25 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_dish_recipe_sub_recipe_alter_sharedrecipe_dish_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish_recipe',
            name='sub_recipe',
        ),
    ]