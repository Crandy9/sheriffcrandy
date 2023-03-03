from django.contrib import admin
from .models import Lctec_User


# Register your models here.
@admin.register(Lctec_User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        # put all other fields you want to be shown in listing
        'username',
    )
    readonly_fields = ['id','date_added']