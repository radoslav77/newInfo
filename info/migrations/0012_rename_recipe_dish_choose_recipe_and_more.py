# Generated by Django 4.0.3 on 2022-04-17 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_dish_recipe_portions_sharedrecipe_portions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='recipe',
            new_name='choose_recipe',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='sub_recipe',
            new_name='choose_subrecipe',
        ),
    ]
