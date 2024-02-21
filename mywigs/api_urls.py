# mywigs/api_urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WigViewSet

router = DefaultRouter()
router.register(r'wigs', WigViewSet, basename='wig')
