""" Category model."""
from django.db import models
from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    