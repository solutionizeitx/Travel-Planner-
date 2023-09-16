from django.contrib import admin

from PackageApp.models import Package,PackageType
class PackageAdmin(admin.ModelAdmin):
    list_filter = ["is_banner","is_best_deals", "is_trending","type__name"]
    list_display = ["name","rate","is_banner","is_trending","is_best_deals","location","type"]
    search_fields = ["name"]
    pass
class PackageTypeAdmin(admin.ModelAdmin):
    list_filter = [ "name","price"]
    list_display = ["name","price","details","is_active"]
    search_fields = ["name"]
    pass

# Register your models here.

admin.site.register(Package,PackageAdmin)
admin.site.register(PackageType,PackageTypeAdmin)
