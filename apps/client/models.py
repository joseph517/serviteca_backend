from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El campo correo electrónico es obligatorio.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser debe tener is_superuser=True.")

        return self.create_user(email, password, **extra_fields, user_name=email)

class Client(AbstractBaseUser, PermissionsMixin):

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
    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    password = models.CharField(
        max_length=128, 
        null=False, 
        blank=False,
        default=None,
    )


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        related_name="client_groups",
        related_query_name="client",
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="client_permissions",
        related_query_name="client",
        verbose_name='user permissions'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "last_name", "number_phone"]

    def __str__(self):
        return self.user_name