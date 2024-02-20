# mywigs/serializers.py
from rest_framework import serializers
from .models import Wig

class WigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wig
        fields = '__all__'
