from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Client

# Register your models here.


@register(Client)
class ClientAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'last_name',
        'email',
        'number_phone',
        'user_name'
    )
    search_fields = ('user_name',)
