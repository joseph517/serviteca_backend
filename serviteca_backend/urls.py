from django.contrib import admin
from django.urls import path, include
from apps.client.api.views import ObtainTokenPairView, TokenRefreshView
from apps.mechanic.api.urls import urlpatterns as mechanic_urls
from apps.vehicle.api.urls import urlpatterns as vehicle_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/client/', include('apps.client.api.urls')),
    path('api/token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/mechanic/', include(mechanic_urls)),
    path('api/vehicle/', include(vehicle_urls))
]
