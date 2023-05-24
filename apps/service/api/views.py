from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Service, ServiceType, ServiceHistory
from .serializers import ServiceSerializer, ServiceTypeSerializer, ServiceHistorySerializer


# Vistas para la aplicación de servicios

class CreateServiceAPIVIEW(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]


class UpdateServiceAPIVIEW(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteServiceAPIVIEW(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()


class ListServiceAPIVIEW(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]


# Vistas para la aplicación de tipos de servicios

class CreateServiceTypeAPIVIEW(generics.CreateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [IsAuthenticated]


class UpdateServiceTypeAPIVIEW(generics.UpdateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteServiceTypeAPIVIEW(generics.DestroyAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()


class ListServiceTypeAPIVIEW(generics.ListAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [IsAuthenticated]


# Vistas para la aplicación de historial de servicios

class CreateServiceHistoryAPIVIEW(generics.CreateAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    permission_classes = [IsAuthenticated]


class UpdateServiceHistoryAPIVIEW(generics.UpdateAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteServiceHistoryAPIVIEW(generics.DestroyAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()


class ListServiceHistoryAPIVIEW(generics.ListAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    permission_classes = [IsAuthenticated]
