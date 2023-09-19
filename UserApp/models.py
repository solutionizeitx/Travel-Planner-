from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    mobile_number=models.CharField(max_length=15,unique=True,null=True,blank=True)

