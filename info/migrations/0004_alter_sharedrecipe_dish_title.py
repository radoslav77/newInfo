# Generated by Django 4.0.3 on 2022-03-25 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_remove_dish_recipe_sub_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedrecipe',
            name='dish_title',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='info.dish_recipe'),
        ),
    ]
