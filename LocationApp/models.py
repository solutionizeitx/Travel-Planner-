from django.db import models

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=15,unique=True)
    is_active=models.BooleanField(default=False)
    def __str__(self):
        return self.name