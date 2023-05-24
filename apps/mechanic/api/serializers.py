from rest_framework import serializers
from apps.mechanic.models import Mechanic

class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '__all__'
