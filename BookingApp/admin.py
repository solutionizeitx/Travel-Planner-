from django.contrib import admin

# Register your models here.
class BookingAdmin(admin.ModelAdmin):

    list_display = ["Hotel","Hotel_Id","Hotel_name","Package_name","Package_Id","Package_price","Hotel_price","Total_price","Booking_date_from","Booking_date_to","Number_of_People","is_paid","Booking_status"]
    search_fields = ["name"]
    pass


admin.site.register(Hotel,HotelAdmin)