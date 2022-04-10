# Generated by Django 4.0.3 on 2022-04-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_beverage_date_dish_date_dish_recipe_date_menu_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('unit', models.CharField(choices=[('g', 'g'), ('kg', 'kg')], max_length=200)),
                ('amout', models.IntegerField()),
                ('calory', models.FloatField()),
            ],
        ),
    ]
