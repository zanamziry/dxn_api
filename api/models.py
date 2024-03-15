from enum import unique
from django.db import models

# Create your models here.
class ServiceCenter(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=64)
            
    def __str__(self) -> str:
        return f'{self.id} : {self.name}'

class Agent(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
            
    def __str__(self) -> str:
        return self.username

class Product(models.Model):
    id = models.CharField(max_length=12,primary_key=True)
    name = models.CharField(max_length=128)
    name_ar = models.CharField(max_length=128,blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=6)
    old_price = models.DecimalField(decimal_places=2,max_digits=6)
    pv = models.DecimalField(null=True, decimal_places=2,max_digits=5)
    available = models.BooleanField(default=True)
    image = models.ImageField(default=None)
    hide = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.id} : {self.name}'

class SiteSetting(models.Model):
    dollarvalue = models.DecimalField(decimal_places=2,max_digits=6)

    def __str__(self) -> str:
        return f'1$ = {self.dollarvalue}'