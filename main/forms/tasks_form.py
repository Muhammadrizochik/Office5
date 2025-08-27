from django import forms
from main.models.tasks import Tasks as Task
 
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("status", )

class TaskUpdateManagerForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ("created_by", )


class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ("created_by", "status")