from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.mechanic.models import Mechanic
from apps.mechanic.api.serializers import MechanicSerializer

class MechanicListAPIView(generics.ListAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    permission_classes = [IsAuthenticated]

class MechanicCreateAPIView(generics.CreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    permission_classes = [IsAuthenticated]

class MechanicUpdateAPIView(generics.UpdateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    permission_classes = [IsAuthenticated]

class MechanicDeleteAPIView(generics.DestroyAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    permission_classes = [IsAuthenticated]
