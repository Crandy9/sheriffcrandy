# Generated by Django 4.1.4 on 2023-04-26 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flps_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flp',
            options={},
        ),
        migrations.AlterModelTable(
            name='flp',
            table='flps',
        ),
    ]