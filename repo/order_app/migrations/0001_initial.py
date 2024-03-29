# Generated by Django 4.1.4 on 2023-04-20 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flps_app', '0001_initial'),
        ('tracks_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('address1', models.CharField(blank=True, max_length=100, null=True)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('statePref', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=100, null=True)),
                ('date_order_created', models.DateTimeField(auto_now=True)),
                ('usd_paid_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('jpy_paid_amount', models.IntegerField(blank=True, default=0, null=True)),
                ('free_download', models.BooleanField(blank=True, default=False, null=True)),
                ('stripe_token', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Stripe Order (for FLPs and tracks)',
                'verbose_name_plural': 'Stripe Orders (for FLPs and tracks)',
                'ordering': ['-date_order_created'],
            },
        ),
        migrations.CreateModel(
            name='OrderTrackItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order_created', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_items', to='order_app.order')),
                ('track', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='track_items', to='tracks_app.track')),
            ],
            options={
                'verbose_name': 'Track Orders',
                'verbose_name_plural': 'Track Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderFlpItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order_created', models.DateTimeField(auto_now=True)),
                ('flp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flp_items', to='flps_app.flp')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flp_items', to='order_app.order')),
            ],
            options={
                'verbose_name': 'FLP Orders',
                'verbose_name_plural': 'FLP Orders',
            },
        ),
    ]
