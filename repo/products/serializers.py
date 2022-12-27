# manually created serializers.py file created to turn DB data into JSON to be used by frontend
from rest_framework import serializers
from .models import *

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track 
        # configure which fields we want to use in frontend. Data is a tuple
        # don't need to include slug field
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "description",
            "usd_price",
            "jpy_price",         
            "get_track",
            "get_sample",
            "get_cover_art",
            "date_added",
        )