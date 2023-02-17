# manually created urls.py file

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tracks_app import views

urlpatterns = [
    # serialized track data accessible from api at DOMAIN/api/v1/latest-tracks/
    path('tracks/', views.TracksList.as_view()),
] 