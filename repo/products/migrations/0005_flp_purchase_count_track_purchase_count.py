# Generated by Django 4.1.4 on 2023-01-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_flp'),
    ]

    operations = [
        migrations.AddField(
            model_name='flp',
            name='purchase_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='track',
            name='purchase_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]