# Generated by Django 4.1.4 on 2023-03-08 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0010_alter_order_address1_alter_order_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='free_download',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
