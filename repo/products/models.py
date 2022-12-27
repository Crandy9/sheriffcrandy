from django.db import models
from django.conf import settings

# audio file product model check out pydub https://github.com/jiaaro/pydub
class Track(models.Model):
    # track name
    title = models.CharField(default='', max_length=255)
    # description (not req'd)
    description = models.CharField(default='', max_length=255, blank=True, null=True)
    # price usd
    usd_price = models.DecimalField(default =0, max_digits=10, decimal_places=2, blank=True)
    # price jpy
    jpy_price = models.IntegerField()
    # aURL ddress of song title
    slug = models.SlugField()
    # song files
    # blank=True is for forms (like admin page)
    # null=True is for null values in DB
    track = models.FileField(upload_to='tracks', blank=True, null=True)
    # sample (approx 30 seconds preview of song to prevent free downloads)
    sample = models.FileField(upload_to='samples', blank=True, null=True)
    # thumbail for audio track art
    cover_art = models.ImageField(upload_to='cover_art', blank=True, null=True)
    # datetime stamp
    date_added = models.DateTimeField(auto_now_add=True)


    # order Tracks by title in the backend
    class Meta:
        # it is a tuple so you need to add a comma so it can be iterable
        ordering = ('title',)

    # string representation of object
    def __str__(self):
        return self.title
    
    # get url of track for frontend
    def get_absolute_url(self):
        return f'/{self.slug}/'

    # get all static files (images, audio tracks, etc) for frontend
    def get_track(self):
        if self.track:
            return settings.env('DOMAIN') + self.track.url
        return ''

    def get_sample(self):
        if self.sample:
            return settings.env('DOMAIN') + self.sample.url
        return ''

    def get_cover_art(self):
        if self.cover_art:
            return settings.env('DOMAIN') + self.cover_art.url
        return ''
