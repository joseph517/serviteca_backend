from rest_framework.permissions import IsAuthenticated

class CustomIsAuthenticated(IsAuthenticated):
    message = "No tiene los permisos para acceder a la vista"