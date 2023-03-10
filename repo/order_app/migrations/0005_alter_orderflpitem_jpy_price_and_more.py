# Generated by Django 4.1.4 on 2023-03-03 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0004_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderflpitem',
            name='jpy_price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='orderflpitem',
            name='usd_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8),
        ),
    ]
