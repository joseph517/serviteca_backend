from django.urls import path
from .views import MechanicListAPIView, MechanicCreateAPIView, MechanicUpdateAPIView, MechanicDeleteAPIView

urlpatterns = [
    path('create/', MechanicCreateAPIView.as_view(), name='create_mechanic'),
    path('update/<int:pk>/', MechanicUpdateAPIView.as_view(), name='update_mechanic'),
    path('delete/<int:pk>/', MechanicDeleteAPIView.as_view(), name='delete_mechanic'),
    path('list/', MechanicListAPIView.as_view(), name='list_mechanic'),
]
