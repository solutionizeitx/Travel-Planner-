from django.contrib import admin

from BookingApp.models import Booking


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_filter = ["hotel_name","packageName","total_price"]
    list_display = ["hotel","hotel_id","hotel_name","packageName","package_price","hotel_price","package_id","total_price","booking_date_from","booking_date_to","number_of_people","is_paid","booking_status"]
    search_fields = ["hotel_name"]

    pass


admin.site.register(Booking,BookingAdmin)