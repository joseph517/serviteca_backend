from django.db import models

from apps.client.models import *
from apps.vehicle.models import *
from apps.mechanic.models import *

# Create your models here.

class ServiceType(models.Model):
    mechanic = models.ForeignKey(
        Mechanic,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='service_types'
    )

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        default=None
    )

    description = models.TextField()

    class Meta:
        verbose_name = 'Tipo de Servicio'
        verbose_name_plural = 'Tipos de Servicios'

    def __str__(self):
        return self.name


class Service(models.Model):

    service_type = models.ForeignKey(
        ServiceType,
        on_delete=models.CASCADE
    )


    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        null=False
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        null=False,
    )

    mechanic = models.ForeignKey(
        Mechanic,
        on_delete=models.PROTECT,
        null=False
    )

    datetime = models.DateTimeField()
    details = models.TextField(
        blank=True,
        null=False,
        default=None
    )
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    is_completed = models.BooleanField(default=False)
    note = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return f'{self.service_type.name} para {self.vehicle}'

    def cancel(self):
        self.delete()

class ServiceHistory(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Historial de Servicio'
        verbose_name_plural = 'Historiales de Servicios'

    def __str__(self):
        return f'Servicio {self.service.service_type.name} para {self.client}'