from django import forms
from main.models.tasks import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']

class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =

        from django.contrib import admin
        from .models import Contact

        admin.site.register(Contact)