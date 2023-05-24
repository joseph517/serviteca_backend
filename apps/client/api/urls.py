from django.urls import path
from .views import CreateClientView, UpdateClientView, DeleteClientView, ListClientView

urlpatterns = [
    path('create/', CreateClientView.as_view(), name='create_client'),
    path('update/<int:pk>/', UpdateClientView.as_view(), name='update_client'),
    path('delete/<int:pk>/', DeleteClientView.as_view(), name='delete_client'),
    path('list/', ListClientView.as_view(), name='list_client'),
]
