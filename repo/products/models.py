from django.db import models
from main_project import settings
# audio libs
from pydub import AudioSegment
from pydub.playback import play
from django.core.files import File
from pathlib import Path
import os


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
    # uploads to /media/tracks dir
    track = models.FileField(upload_to='tracks', blank=True, null=True)
    # sample (approx 30 seconds preview of song to prevent free downloads)
    # uploads to /media/samples dir
    sample = models.FileField(upload_to='samples', blank=True, null=True)
    # thumbail for audio track art
    # uploads to /media/cover_art dir
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
        # if this sample is already created
        if self.sample:
            return settings.env('DOMAIN') + self.sample.url
        # else if the song is uploaded but the sample hasn't been created, create it and save it to DB
        else:
            if self.track:
                self.sample = self.make_sample(self.track)
                self.save()
                return settings.env('DOMAIN') + self.sample.url
        # else if the track isn't created, return an empty string
        return ''

    def get_cover_art(self):
        if self.cover_art:
            return settings.env('DOMAIN') + self.cover_art.url
        return ''

    # generate the 30 second splice sample
    # audio file product model check out pydub https://github.com/jiaaro/pydub
    def make_sample(self, track):
        # make a new temp path var to temporarily store the new sample
        tmp_path = '/tmp/'
        print("Full song untouched: " + str(track) + '\n')
        # restring sample title name
        song_full_path = str(track)
        song_file = song_full_path.replace('tracks/','')
        song_name = song_file.replace('.wav','')

        # open wav file
        # play runs this and saves in /tmp dir
        '''
        Input #0, wav, from '/tmp/tmpf22q16d_.wav':   0KB sq=    0B f=0/0   
        Duration: 00:03:51.46, bitrate: 2822 kb/s
        Stream #0:0: Audio: pcm_s32le ([1][0][0][0] / 0x0001), 44100 Hz, 2 channels, s32, 2822 kb/s
        '''
        full_song = AudioSegment.from_wav(track)

        # 50 seconds (in miliseconds)
        if full_song.duration_seconds > 50:
            print ("Song length: " + str(full_song.duration_seconds))
            song_limit = 50 * 1000
            sample = full_song[:song_limit]
        else:
            print ("Song length: " + str(full_song.duration_seconds))
            song_limit = 30 * 1000
            sample = full_song[:song_limit]


        # fade in/out the sample
        faded_sample = sample.fade_in(2000).fade_out(3000)
        
        # full sample path
        sample_path = tmp_path + song_name + "_sample.mp3"

        # export to /tmp path
        faded_sample.export(sample_path, format="mp3")

        # now open that file so Django can read it
        converted_sample = File(
                file=open(sample_path, 'rb'),
                name=Path(sample_path)
            )
        converted_sample.name = Path(sample_path).name
        converted_sample.content_type = 'audio/mpeg'
        converted_sample.size = os.path.getsize(sample_path)
        
        return converted_sample
