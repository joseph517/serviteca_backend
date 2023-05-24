from rest_framework import serializers
from apps.vehicle.models import *

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'client', 'brand', 'model', 'year', 'plate_number']