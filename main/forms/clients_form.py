from django import forms
from main.models.clients import Client
from django.core.exceptions import ValidationError

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['phone']

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if Client.objects.filter(phone=phone).exists():
            raise ValidationError("Bu telefon raqami allaqachon ro'yhatdan o'tgan")
        return phone