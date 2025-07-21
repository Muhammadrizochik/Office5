from django import forms
from main.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']

class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'