# Generated by Django 4.1.4 on 2023-04-26 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lctec_user', '0004_alter_lctec_user_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='user_cart',
        ),
    ]
