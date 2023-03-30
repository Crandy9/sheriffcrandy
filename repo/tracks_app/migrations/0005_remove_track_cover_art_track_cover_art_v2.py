# Generated by Django 4.1.4 on 2023-03-30 05:17

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tracks_app', '0004_alter_track_cover_art'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='cover_art',
        ),
        migrations.AddField(
            model_name='track',
            name='cover_art_v2',
            field=imagekit.models.fields.ProcessedImageField(blank=True, max_length=255, null=True, upload_to='cover_art'),
        ),
    ]
