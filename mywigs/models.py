# mywigs/models.py
from django.db import models
from django.contrib.auth import get_user_model

class Wig(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=32)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    curl_pattern = models.CharField(max_length=16, choices=[('curly', 'Curly'), ('straight', 'Straight')])
    density = models.DecimalField(max_digits=5, decimal_places=2, help_text="Density of the wig in percentage")
    hair_origin = models.CharField(max_length=16, choices=[('brazilian', 'Brazilian'), ('peruvian', 'Peruvian')])
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
