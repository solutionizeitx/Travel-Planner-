from django.db import models

from HotelApp.models import Hotel
from PackageApp.models import Package, PackageType
from UserApp.models import UserModel


# Create your models here.
class Booking(models.Model):
      created_date=models.DateField(auto_now_add=True,null=True,blank=True)
      updated_date=models.DateField(auto_now=True,null=True,blank=True)

      package=models.ForeignKey(Package,on_delete=models.PROTECT)
      packageId=models.IntegerField(null=True,blank=True)

      packageName=models.CharField(max_length=15)

      hotel=models.ForeignKey(Hotel,on_delete=models.PROTECT)
      hotelId=models.IntegerField(null=True,blank=True)
      hotel_name=models.CharField(max_length=25)
      type=models.ForeignKey(PackageType,on_delete=models.PROTECT)
      typeId=models.IntegerField(null=True,blank=True)
      typeName=models.CharField(max_length=25)
      package_price=models.DecimalField(max_digits=20,decimal_places=2)
      hotel_price=models.DecimalField(max_digits=20,decimal_places=2)
      total_price=models.DecimalField(max_digits=20,decimal_places=2)
      booking_date_from=models.DateTimeField()
      booking_date_to=models.DateTimeField()

      discount=models.DecimalField(max_digits=10,decimal_places=2)
      number_of_people=models.IntegerField()
      is_paid=models.BooleanField(default=False)
      booking_status=models.BooleanField(default=False)
      user=models.ForeignKey(UserModel,on_delete=models.PROTECT)
