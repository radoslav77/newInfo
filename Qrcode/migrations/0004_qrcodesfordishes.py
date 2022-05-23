# Generated by Django 4.0.3 on 2022-05-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qrcode', '0003_genaratecode_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRcodesForDishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('outlet', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='media')),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
