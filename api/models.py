from enum import unique
from django.db import models

# Create your models here.
class ServiceCenter(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=64)
            
    def __str__(self) -> str:
        return self.name

class Agent(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
            
    def __str__(self) -> str:
        return self.username

class Product(models.Model):
    id = models.CharField(max_length=12,primary_key=True,verbose_name="ID")
    name = models.CharField(max_length=128,verbose_name="Name")
    name_ar = models.CharField(max_length=128,blank=True,null=True,verbose_name="Arabic Name")
    price = models.DecimalField(decimal_places=2,max_digits=6,verbose_name="Price")
    old_price = models.DecimalField(decimal_places=2,max_digits=6, verbose_name="Old Price")
    pv = models.DecimalField(null=True, decimal_places=2,max_digits=5,verbose_name="Points")
    available = models.BooleanField(default=True,verbose_name="Available")
    image = models.ImageField(null=True, blank=True, upload_to = 'products/' ,verbose_name="Picture")
    hide = models.BooleanField(default=False,verbose_name="Hidden")

    def __str__(self) -> str:
        return self.name

class SiteSetting(models.Model):
    dollarvalue = models.DecimalField(decimal_places=2,max_digits=6,verbose_name="$1 Value")
    def __str__(self) -> str:
        return self.dollarvalue