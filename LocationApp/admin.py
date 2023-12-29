from django.contrib import admin

# Register your models here.
from .models import Location
from django.contrib import admin
from LocationApp.models import Location
class LocationAdmin(admin.ModelAdmin):
    list_filter = ["is_active"]
    list_display = ["name","is_active"]
    search_fields = ["name"]
    pass
admin.site.register(Location,LocationAdmin)
