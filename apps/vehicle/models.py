from django.db import models

from apps.client.models import Client

# Create your models here.

class Vehicle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.IntegerField()
    plate_number = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return f'{self.brand} {self.model} ({self.year}) - {self.plate_number}'
