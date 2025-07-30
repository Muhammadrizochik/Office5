from django.db import models
from django.contrib.auth.models import User
from main.models.base import BaseModel

class Client(BaseModel):
    f_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='clients')

    def __str__(self):
        return self.f_name

    class Meta:
        ordering = ['-added_at']