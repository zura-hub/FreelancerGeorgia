from django import forms
from .models import Freelancer

class FreelancerForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ['cover_img', 'name', 'last_name', 'profession', 'experience', 'skills', 'cover_letter', ]
