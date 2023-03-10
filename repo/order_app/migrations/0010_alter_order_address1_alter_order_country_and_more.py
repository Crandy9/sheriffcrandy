# Generated by Django 4.1.4 on 2023-03-08 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0009_alter_order_stripe_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='statePref',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
