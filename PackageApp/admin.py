from django import forms
from django.contrib import admin

from PackageApp.models import Package, PackageType
from PIL import Image


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'

    def clean_banner_image(self):
        banner_image = self.cleaned_data.get('banner_image')

        # Check if the image has the correct dimensions
        if banner_image:
            # Open the image using Pillow
            with Image.open(banner_image) as img:
                width, height = img.size
                if width != 1200 or height != 600:
                    raise forms.ValidationError(
                        "Image must have dimensions of 1200x600 pixels.")

        return banner_image


class PackageAdmin(admin.ModelAdmin):
    form = PackageForm
    list_filter = ["is_banner", "is_best_deals", "is_trending", "type__name"]
    list_display = ["name", "rate", "is_banner",
                    "is_trending", "is_best_deals", "location", "type"]
    search_fields = ["name"]


class PackageTypeAdmin(admin.ModelAdmin):
    list_filter = ["name", "price"]
    list_display = ["name", "price", "details", "is_active"]
    search_fields = ["name"]
    pass

# Register your models here.


admin.site.register(Package, PackageAdmin)
admin.site.register(PackageType, PackageTypeAdmin)
