from django import forms
from main.models.clients import Client
from django.core.exceptions import ValidationError

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['f_name', 'email', 'phone', 'address', 'created_by']

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        qs = Client.objects.filter(phone=phone)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Bu telefon raqami allaqachon ro'yxatdan o'tgan")
        return phone
