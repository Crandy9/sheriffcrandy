from django.contrib import admin
from .models import Order, OrderFlpItem, OrderTrackItem

# Register your models here.
@admin.register(Order)
class AdminClassName(admin.ModelAdmin):
    readonly_fields = ['date_order_created', 'id']

@admin.register(OrderFlpItem)
class AdminClassName(admin.ModelAdmin):
    readonly_fields = ['date_order_created','id']

@admin.register(OrderTrackItem)
class AdminClassName(admin.ModelAdmin):
    readonly_fields = ['date_order_created','id']