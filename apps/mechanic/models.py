from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Mechanic(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False,
        blank=False,
        default=None,
        unique=True
    )

    user_name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        default=None
    )

    name = models.CharField(
        max_length=255, 
        null=False,
        blank=False,
        default=None,
    )

    last_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,    
    )

    email = models.EmailField(unique=True)

    number_phone = PhoneNumberField(
        verbose_name="Celular",
        null=False,
        blank=False,
        unique=True
    )

    password = models.CharField(
        max_length=128, 
        null=True, 
        blank=False,
        default=None,
    )

    class Meta:
        verbose_name = 'Mecanico'
        verbose_name_plural = 'Mecanicos'

    def __str__(self):
        return self.name