# mywigs/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import viewsets
from .models import Wig
from .serializers import WigSerializer


class WigViewSet(viewsets.ModelViewSet):
    queryset = Wig.objects.all()
    serializer_class = WigSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
