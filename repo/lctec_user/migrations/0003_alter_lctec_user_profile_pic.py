# Generated by Django 4.1.4 on 2023-04-24 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lctec_user', '0002_lctec_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lctec_user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='pfps'),
        ),
    ]