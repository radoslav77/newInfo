# Generated by Django 4.0.3 on 2022-04-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_calory'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish_recipe',
            name='dish_title',
            field=models.CharField(default='new', max_length=200),
        ),
    ]