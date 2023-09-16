from django.contrib import admin

from HotelApp.models import Hoteltype
from HotelApp.models import Hotel


# Register your models here.
class HoteltypeAdmin(admin.ModelAdmin):

    list_display = ["name","rate","is_active"]
    search_fields = ["name"]
    pass

class HotelAdmin(admin.ModelAdmin):
    list_filter = ["is_active"]
    list_display = ["name","rate","is_active","actual_price","description","location","type"]
    search_fields = ["name","location"]
    pass
admin.site.register(Hoteltype,HoteltypeAdmin)
admin.site.register(Hotel,HotelAdmin)