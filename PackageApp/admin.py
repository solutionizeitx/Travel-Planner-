from django.contrib import admin

from PackageApp.models import Package,PackageType


# Register your models here.

admin.site.register(Package)
admin.site.register(PackageType)
