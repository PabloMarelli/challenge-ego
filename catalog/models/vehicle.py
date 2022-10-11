"""Vehicle model"""
from django.db import models
from core.models import BaseModel


class Vehicle(BaseModel):
    
    name = models.CharField(max_length=255)
    model = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE)