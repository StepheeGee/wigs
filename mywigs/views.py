# mywigs/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Wig
from .serializers import WigSerializer
from django.shortcuts import render
from django.http import HttpResponse

class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Wigs API!"})

class WigViewSet(viewsets.ModelViewSet):
    queryset = Wig.objects.all()
    serializer_class = WigSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
