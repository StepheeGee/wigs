# mywigs/urls.py

from django.urls import path, include
from .views import HomeView
from .api_urls import router

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
