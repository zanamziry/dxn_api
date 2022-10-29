from enum import unique
from django.db import models

# Create your models here.
class Agent(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.id} : {self.username}'
    