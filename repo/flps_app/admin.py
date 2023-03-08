from django.contrib import admin
from .models import *

@admin.register(Flp)
class AdminClassName(admin.ModelAdmin):
    readonly_fields = ['pk', 'downloads', 'date_added']