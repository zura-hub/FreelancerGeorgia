from django import forms
from .models import Temp
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class TempForms(forms.ModelForm):  # corrected from TempFroms to TempForms
    class Meta:
        model = Temp
        fields = ['title', 'designe', 'link', 'phone', 'mail', 'price']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': "Title"
            }),
            'link': TextInput(attrs={
                'placeholder': "GitHub Deployment Link"
            }),
            'phone': TextInput(attrs={
                'placeholder': "phone number"
            }),
            'mail': TextInput(attrs={
                'placeholder': "mail"
            }),
            'price': TextInput(attrs={
                'placeholder': "price",
            }),
        }