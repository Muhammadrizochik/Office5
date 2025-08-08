from django import forms
from main.models.tasks import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']

class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
<<<<<<< HEAD
        fields =['name']
=======
        fields = ["title"]
>>>>>>> c4128a290fe4b0c0c7c2241136678a2295746993
