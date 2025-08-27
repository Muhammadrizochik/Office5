from django import forms
from main.models.tasks import Tasks as Task
 
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ("status", "created_by")


class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ("status", "created_by")