# Generated by Django 4.0.3 on 2022-05-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qrcode', '0009_alter_qrcodesfordishes_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodesfordishes',
            name='img',
            field=models.ImageField(upload_to='media'),
        ),
    ]
