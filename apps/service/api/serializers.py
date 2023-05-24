from rest_framework import serializers
from apps.service.models import *

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'name', 'description']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'vehicle', 'service_type', 'datetime', 'details', 'total_cost', 'is_completed', 'note']

class ServiceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHistory
        fields = ['id', 'client', 'service']