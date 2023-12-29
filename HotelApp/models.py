from django.db import models

from LocationApp.models import Location
from PackageApp.models import PackageType


class Hoteltype(models.Model):
    name = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=False)
    rate = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    banner_image = models.ImageField(upload_to="media", null=True, blank=True)
    normal_image = models.ImageField(upload_to="media", null=True, blank=True)
    name = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=False)
    rate = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    actual_price = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=False)
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, null=True, blank=True)
    type = models.ForeignKey(
        Hoteltype, on_delete=models.PROTECT, null=True, blank=True)
    address = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.name
