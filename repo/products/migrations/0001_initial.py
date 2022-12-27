# Generated by Django 4.1.4 on 2022-12-27 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('usd_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('jpy_price', models.IntegerField()),
                ('slug', models.SlugField()),
                ('track', models.FileField(blank=True, null=True, upload_to='tracks')),
                ('sample', models.FileField(blank=True, null=True, upload_to='samples')),
                ('cover_art', models.ImageField(blank=True, null=True, upload_to='cover_art')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]