from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True