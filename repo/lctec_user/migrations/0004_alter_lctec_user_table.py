# Generated by Django 4.1.4 on 2023-04-26 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lctec_user', '0003_alter_lctec_user_profile_pic'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='lctec_user',
            table='users',
        ),
    ]