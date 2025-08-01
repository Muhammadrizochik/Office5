<<<<<<< HEAD
from django import forms
from main.models.clients import Client
from django.core.exceptions import ValidationError
=======
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from main.models.clients import Client
>>>>>>> 65ad6bbf51430822ffa2476fe28b88e4036e5da8

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['phone']

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if Client.objects.filter(phone=phone).exists():
            raise ValidationError("Bu telefon raqami allaqachon ro'yhatdan o'tgan")
        return phone