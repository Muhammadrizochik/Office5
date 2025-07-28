from django.db import models
from django.contrib.auth.models import User
from models.base import BaseModel

class Task(BaseModel):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    def __str__(self):
        return self.title

from django.db import models

class Tasks(BaseModel):
    name = models.CharField(max_length=255)
    doer = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name


