# mywigs/urls.py
from rest_framework.routers import DefaultRouter
from .views import WigViewSet

router = DefaultRouter()
router.register(r'wigs', WigViewSet, basename='wig')
urlpatterns = router.urls
