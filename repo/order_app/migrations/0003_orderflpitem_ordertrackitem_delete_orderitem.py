# Generated by Django 4.1.4 on 2023-03-01 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracks_app', '0001_initial'),
        ('flps_app', '0001_initial'),
        ('order_app', '0002_alter_orderitem_flp_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderFlpItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd_flp_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('jpy_flp_price', models.IntegerField(blank=True, default=0, null=True)),
                ('flp_quantity', models.IntegerField(default=0)),
                ('flp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flp_items', to='flps_app.flp')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flp_items', to='order_app.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderTrackItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd_track_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('jpy_track_price', models.IntegerField(blank=True, default=0, null=True)),
                ('track_quantity', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_items', to='order_app.order')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_items', to='tracks_app.track')),
            ],
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]