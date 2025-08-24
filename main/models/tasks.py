from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(help_text="Vazifa haqida qisqacha")

    STATUS_CHOICES = [
        ('new', 'Yangi'),
        ('process', 'Jarayyonda'),
        ('done', 'Tugallangan'),
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='new')

    doer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, related_name='tasks')

    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name