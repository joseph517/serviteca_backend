from apps.client.models import Client
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agregar atributos personalizados al token
        token['nombre'] = user.name
        token['apellido'] = user.last_name

        return token

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('email', 'password')

    def create(self, validated_data):
        user = Client.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

class ClientSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField()

    class Meta:
        model = Client
        fields = ('user_name', 'name', 'last_name', 'email', 'number_phone', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        client = Client.objects.create(
            user_name=validated_data['user_name'],
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            number_phone=validated_data['number_phone'],
            password=validated_data['password'],
        )
        client.set_password(validated_data['password'])
        client.save()

        return client


class ClientUpdateSerializer(ClientSerializer):
    class Meta(ClientSerializer.Meta):
        extra_kwargs = {
            "last_name": {"required": False},
            "email": {"required": False},
            "number_phone": {"required": False},
        }

class DeleteClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
