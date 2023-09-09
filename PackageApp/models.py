from django.db import models
from LocationApp.models import Location
class PackageType(models.Model):
    name = models.CharField(max_length=15, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    details = models.TextField(null=True,blank=False)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Package(models.Model):
    name=models.CharField(max_length=15,unique=True)
    rate=models.DecimalField(max_digits=20,decimal_places=2)

    actual_price=models.DecimalField(max_digits=20,decimal_places=2)
    banner_image=models.ImageField(upload_to="media")
    normal_image = models.ImageField(upload_to="media")
    is_banner=models.BooleanField(default=False)
    is_best_deals=models.BooleanField(default=False)
    is_trending=models.BooleanField(default=False)
    location=models.ForeignKey(Location,on_delete=models.PROTECT)
    type = models.ForeignKey(PackageType, on_delete=models.PROTECT)
    description=models.TextField(null=True,blank=False)
    def __str__(self):
        return self.name


