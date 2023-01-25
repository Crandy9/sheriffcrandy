from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# get newest songs using APIView from django rest_framework
class TracksList(APIView):
    def get(self, request, format=None):
        tracks = Track.objects.all() # getting the first four objects or "latest" objects
        # convert these objects into JSON. Pass in tracks and set many=True because we have more than one obj
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)


# get newest songs using APIView from django rest_framework
class FlpsList(APIView):
    def get(self, request, format=None):
        flps = Flp.objects.all() # getting the first four objects or "latest" objects
        # convert these objects into JSON. Pass in tracks and set many=True because we have more than one obj
        serializer = FlpSerializer(flps, many=True)
        return Response(serializer.data)