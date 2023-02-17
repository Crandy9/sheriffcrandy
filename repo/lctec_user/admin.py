from django.contrib import admin
from .models import Lctec_User


# Register your models here.
@admin.register(Lctec_User)
class CustomUserAdmin(admin.ModelAdmin):
    pass