
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Vacancy
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class SignUpForm(UserCreationForm):
    user = forms.UserCreationForm()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'currency', 'budget', 'data']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Job Title"
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Job Description"
            }),
            'budget': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "budget"
            }),
            'currency': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "currency"
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "data",
            }),
        }