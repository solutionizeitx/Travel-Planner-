from django.db import models

from HotelApp.models import Hotel
from PackageApp.models import Package, PackageType
from UserApp.models import UserModel


BOOKING_STATUS_PENDING = "pending"
BOOKING_STATUS_CONFIRMED = "confirmed"
BOOKING_STATUS_CANCELLED = "cancelled"
BOOKING_STATUS_COMPLETED = "completed"


BOOKING_STATUS_CHOICES = (
    (BOOKING_STATUS_PENDING, BOOKING_STATUS_PENDING),
    (BOOKING_STATUS_CONFIRMED, BOOKING_STATUS_CONFIRMED),
    (BOOKING_STATUS_CANCELLED, BOOKING_STATUS_CANCELLED),
    (BOOKING_STATUS_COMPLETED, BOOKING_STATUS_COMPLETED),
)

# Create your models here.


class Booking(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_date = models.DateField(auto_now=True, null=True, blank=True)

    package = models.ForeignKey(
        Package, on_delete=models.PROTECT, null=True, blank=True)
    packageId = models.IntegerField(null=True, blank=True)
    packageName = models.CharField(max_length=30, null=True, blank=True)

    hotel = models.ForeignKey(
        Hotel, on_delete=models.PROTECT, null=True, blank=True)
    hotelId = models.IntegerField(null=True, blank=True)
    hotel_name = models.CharField(max_length=30, null=True, blank=True)

    type = models.ForeignKey(
        PackageType, on_delete=models.PROTECT, null=True, blank=True)
    typeId = models.IntegerField(null=True, blank=True)
    typeName = models.CharField(max_length=25, null=True, blank=True)

    package_price = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    hotel_price = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    booking_date_from = models.DateTimeField()
    booking_date_to = models.DateTimeField()

    discount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    number_of_people = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    booking_status = models.CharField(max_length=25, default=BOOKING_STATUS_PENDING,
                                      choices=BOOKING_STATUS_CHOICES)
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT)
