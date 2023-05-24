from django.contrib import admin
from apps.mechanic.models import Mechanic
from django import forms
from django.forms import ModelChoiceField



from apps.service.models import Service, ServiceType, ServiceHistory
from apps.vehicle.models import Vehicle

# Register your models here.
@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class ServiceAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtener el cliente seleccionado en el formulario
        client_id = self.data.get('client', None)
        if client_id:
            # Filtrar los vehículos por el cliente seleccionado
            self.fields['vehicle'].queryset = Vehicle.objects.filter(client_id=client_id)
        else:
            self.fields['vehicle'].queryset = Vehicle.objects.none()

    class Meta:
        model = Service
        fields = '__all__'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'service_type', 'datetime', 'total_cost', 'is_completed')
    search_fields = ('vehicle__brand', 'service_type__name')
    list_filter = ('is_completed',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'vehicle':
            # Obtener el cliente seleccionado en el formulario
            client_id = request.POST.get('client', None)
            if client_id:
                # Filtrar los vehículos por el cliente seleccionado
                kwargs['queryset'] = Vehicle.objects.filter(client_id=client_id)
            else:
                kwargs['queryset'] = Vehicle.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

@admin.register(ServiceHistory)
class ServiceHistoryAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'is_service_completed')
    list_filter = ('service__is_completed',)

    def client(self, obj):
        return obj.service.client
    client.short_description = 'Client'

    def is_service_completed(self, obj):
        return obj.service.is_completed
    is_service_completed.short_description = 'Service Completed'