from django.urls import path
from .views import (
    CreateServiceAPIVIEW,
    UpdateServiceAPIVIEW,
    DeleteServiceAPIVIEW,
    ListServiceAPIVIEW,
    CreateServiceTypeAPIVIEW,
    UpdateServiceTypeAPIVIEW,
    DeleteServiceTypeAPIVIEW,
    ListServiceTypeAPIVIEW,
    CreateServiceHistoryAPIVIEW,
    UpdateServiceHistoryAPIVIEW,
    DeleteServiceHistoryAPIVIEW,
    ListServiceHistoryAPIVIEW
)

urlpatterns = [
    #service
    path('create/', CreateServiceAPIVIEW.as_view(), name='create_service'),
    path('update/<int:pk>/', UpdateServiceAPIVIEW.as_view(), name='update_service'),
    path('delete/<int:pk>/', DeleteServiceAPIVIEW.as_view(), name='delete_service'),
    path('list/', ListServiceAPIVIEW.as_view(), name='list_service'),
    #serviceType
     path('create/', CreateServiceTypeAPIVIEW.as_view(), name='create_servicetype'),
    path('update/<int:pk>/', UpdateServiceTypeAPIVIEW.as_view(), name='update_servicetype'),
    path('delete/<int:pk>/', DeleteServiceTypeAPIVIEW.as_view(), name='delete_servicetype'),
    path('list/', ListServiceTypeAPIVIEW.as_view(), name='list_servicetype'),
    #serviceHistory
    path('create/', CreateServiceHistoryAPIVIEW.as_view(), name='create_servicehistory'),
    path('update/<int:pk>/', UpdateServiceHistoryAPIVIEW.as_view(), name='update_servicehistory'),
    path('delete/<int:pk>/', DeleteServiceHistoryAPIVIEW.as_view(), name='delete_servicehistory'),
    path('list/', ListServiceHistoryAPIVIEW.as_view(), name='list_servicehistory'),
]

