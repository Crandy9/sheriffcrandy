import datetime
from django.db import models
from sheriff_crandy_project import settings
# audio libs
from pydub import AudioSegment
from django.core.files import File
from pathlib import Path
import os


class Flp(models.Model):

    flp_name = models.CharField(default='', max_length=255)
    description = models.CharField(default='', max_length=255, blank=True, null=True)
    usd_price = models.DecimalField(default =0, max_digits=10, decimal_places=2, blank=True)
    jpy_price = models.IntegerField(default =0, blank=True)
    slug = models.SlugField()
    flp_zip = models.FileField(upload_to='flp_zips', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # calling it flp_is_free to distinguish from free tracks in frontend
    flp_is_free = models.BooleanField(default=False, blank=True, null=True)
    purchase_count = models.IntegerField(default=0, blank=True)


    class Meta:
        ordering = ('flp_name',)

    def __str__(self):
        return self.flp_name + ' - Downloads: ' + str(self.purchase_count)
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

    # get flp_zip files
    def get_zips(self):
        if self.flp_zip:
            return settings.env('DOMAIN') + self.flp_zip.url
        return ''