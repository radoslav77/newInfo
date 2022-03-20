# Generated by Django 4.0.3 on 2022-03-20 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=400)),
                ('description', models.TextField(max_length=4000)),
                ('alcohol_type', models.CharField(choices=[('Soft', 'Soft'), ('Coffee', 'Coffee'), ('Tea', 'Tea'), ('Juice', 'Juice'), ('Beer', 'Beer'), ('Wine', 'Wine'), ('Sparkling Wine', 'Sparkling Wine'), ('Spirit', 'Spirit'), ('Shot', 'Shot')], max_length=200)),
                ('alergens', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Dish_Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('outlet', models.CharField(choices=[('Room Service', 'Room Service'), ('Thoe', 'Thoe Randal'), ('Arch Bar', 'Arch Bar'), ('Wellington Lounge', 'Wellington Lounge'), ('Number One', 'Number One'), ('BQT', 'BQT')], max_length=200)),
                ('type_dish', models.CharField(choices=[('Starter', 'Starter'), ('Main', 'Main'), ('Dessert', 'Dessert')], max_length=200)),
                ('recipe', models.TextField(max_length=4000)),
                ('method', models.TextField(max_length=6000)),
                ('picture', models.ImageField(upload_to='media')),
                ('archived', models.BooleanField(default=False)),
                ('shared', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='SharedRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type_dish', models.CharField(choices=[('Starter', 'Starter'), ('Main', 'Main'), ('Dessert', 'Dessert')], max_length=200)),
                ('recipe', models.TextField(max_length=4000)),
                ('method', models.TextField(max_length=6000)),
                ('archived', models.BooleanField(default=False)),
                ('dish_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.dish_recipe')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Pairing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bev_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pairing_Drink', to='info.beverage')),
                ('dish_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pairing_Dish', to='info.dish_recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('dessert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dess', to='info.dish_recipe')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Drink', to='info.beverage')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Main', to='info.dish_recipe')),
                ('starters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Start', to='info.dish_recipe')),
            ],
        ),
        migrations.AddField(
            model_name='dish_recipe',
            name='sub_recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.sharedrecipe'),
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=3000)),
                ('pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='info.dish_recipe')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.dish_recipe')),
                ('sub_recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.sharedrecipe')),
            ],
        ),
    ]
