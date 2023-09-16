from django.contrib import admin


# Register your models here.
from .models import UserModel
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["username","first_name","last_name","email","mobile_number"]
    search_fields = [""]
    pass


admin.site.register(UserModel,UserModelAdmin)
