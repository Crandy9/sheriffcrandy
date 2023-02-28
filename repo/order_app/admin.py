from django.contrib import admin
from .models import Order

# Register your models here.
# Register your models here.
@admin.register(Order)
class AdminClassName(admin.ModelAdmin):
    readonly_fields = []