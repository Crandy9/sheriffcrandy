# Generated by Django 4.1.4 on 2023-03-20 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flps_app', '0003_alter_flp_jpy_price_alter_flp_usd_price'),
        ('tracks_app', '0003_alter_track_jpy_price_alter_track_usd_price'),
        ('lctec_user', '0003_alter_lctec_user_favorite_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flp_cart_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('track_cart_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('total_cart_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('flps_in_cart', models.ManyToManyField(blank=True, to='flps_app.flp')),
                ('tracks_in_cart', models.ManyToManyField(blank=True, to='tracks_app.track')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
