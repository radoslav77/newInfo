# Generated by Django 4.0.3 on 2022-05-22 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Qrcode', '0004_qrcodesfordishes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcodesfordishes',
            name='date',
        ),
        migrations.RemoveField(
            model_name='qrcodesfordishes',
            name='outlet',
        ),
    ]
