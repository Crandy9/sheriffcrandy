# manually created serializers.py file created to turn DB data into JSON to be used by frontend
from rest_framework import serializers
from .models import *
# import User
from django.contrib.auth.models import User


# audio files
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track 
        # configure which fields we want to use in frontend. Data is a tuple
        # will be shown in API at DOMAIN/api/v1/latest-tracks/
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "description",
            "usd_price",
            "jpy_price",         
            # "get_track",
            "get_sample",
            "get_cover_art",
            "date_added",
            "is_free",
            "get_track_duration",
            # "purchase_count"
        )