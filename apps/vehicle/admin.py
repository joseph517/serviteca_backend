from django.contrib import admin

from apps.vehicle.models import Vehicle


# Register your models here.
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('client', 'brand', 'model', 'year', 'plate_number')
    search_fields = ('client__name', 'brand', 'model', 'plate_number')