from django.db import models
from PackageApp.models import Package,PackageType
from UserApp.models import User

# Create your models here.
class Booking(models.Model):
      Created_date=models.DateField()
      Package=models.ForeignKey(Package, on_delete=models.PROTECT)
      Package_Id=models.IntegerField()
      Package_name=models.CharField(max_length=15,unique=True)
      Hotel=models.CharField(max_length=25,unique=True)
      Hotel_Id=models.IntegerField
      Hotel_name=models.CharField(max_length=25,unique=True)
      Type=models.DecimalField(max_digits=20,decimal_places=2)
      Type_Id=models.IntegerField()
      Type_Name=models.CharField(max_length=25,unique=True)
      Package_price=models.DecimalField(max_digits=20,decimal_places=2)
      Hotel_price=models.DecimalField(max_digits=20,decimal_places=2)
      Total_price=models.DecimalField(max_digits=20,decimal_places=2)
      Booking_date_from=models.DateTimeField()
      Booking_date_to=models.DateTimeField()
      User=models.ForeignKey(User, on_delete=models.PROTECT)
      discount=models.DecimalField(max_digits=10,decimal_places=2)
      Number_of_people=models.SmallIntegerField()
      is_paid=models.BooleanField(default=False)
      Booking_status=models.BooleanField(default=False)

