from django.contrib import admin
from .models import *

@admin.register(Track)
class AdminClassName(admin.ModelAdmin):
    readonly_fields = ['pk', 'sample','song_dur', 'purchase_count']

@admin.register(Flp)
class AdminClassName(admin.ModelAdmin):
    readonly_fields = ['pk', 'purchase_count']