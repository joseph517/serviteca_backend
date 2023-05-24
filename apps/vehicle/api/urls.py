from django.urls import path
from .views import (
    CreateVehicleAPIView,
    UpdateVehicleAPIView,
    DeleteVehicleAPIView,
    ListVehicleAPIView,
    UserVehicleListAPIVIEW,
)

urlpatterns = [
    path('create/', CreateVehicleAPIView.as_view(), name='create_vehicle'),
    path('update/<int:pk>/', UpdateVehicleAPIView.as_view(), name='update_vehicle'),
    path('delete/<int:pk>/', DeleteVehicleAPIView.as_view(), name='delete_vehicle'),
    path('list/', ListVehicleAPIView.as_view(), name='list_vehicle'),
    path('user_list/', UserVehicleListAPIVIEW.as_view(), name='user_vehicle_list'),

]
