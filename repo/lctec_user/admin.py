from django.contrib import admin
from .models import Lctec_User, Cart


# Register your models here.
@admin.register(Lctec_User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        # put all other fields you want to be shown in listing
        'username',
    )
    readonly_fields = ['id','date_added']

@admin.register(Cart)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('cart_name', 'Flps', 'Tracks')
    readonly_fields = ['id',]

    def cart_name(self, obj):
        return obj.user.username + "'s cart"

    def Flps(self, obj):
        return ", ".join([flp.flp_name for flp in obj.flps_in_cart.all()])

    def Tracks(self, obj):
        return ", ".join([track.title for track in obj.tracks_in_cart.all()])