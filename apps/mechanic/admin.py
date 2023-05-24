from django.contrib import admin

from apps.mechanic.models import *

# Register your models here.
@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'name', 'last_name')
    search_fields = ('user_name', 'name', 'email')
    list_filter = ('user_name',)