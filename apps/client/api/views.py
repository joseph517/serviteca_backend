from apps.client.models import Client
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, ClientSerializer, ClientUpdateSerializer, DeleteClientSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken



class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        # Agregar el ID del usuario a la respuesta
        data = {
            'refresh': str(refresh),
            'access': str(access_token),
            'user_id': user.id,
            'rol': user.is_staff,
            'name': user.name
        }

        return Response(data)
    

class TokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

class CreateClientView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            if 'UNIQUE constraint failed: client_client.user_name' in str(e):
                return Response({'error': 'El nombre de usuario ya está en uso.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Error interno del servidor.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class ListClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdateClientView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer
    permission_classes = [IsAuthenticated]

class DeleteClientView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = DeleteClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()
