# Generated by Django 4.0.3 on 2022-05-28 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qrcode', '0010_alter_qrcodesfordishes_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodesfordishes',
            name='img',
            field=models.FileField(upload_to='qrcodes'),
        ),
    ]
