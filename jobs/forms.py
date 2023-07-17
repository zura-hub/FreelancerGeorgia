from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class userRegisterForm(UserCreationForm):

    email = forms.EmailField(required = True)
    filed_order = ['username', 'email', 'password1', 'password2' ]


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
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
