from django import forms
from .models import Forms

class CustomerFormClass(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput())
    
    class Meta:
        model = Forms
        fields = ['name', 'email', 'phone', 'country']
        labels = {
            'name': 'Full Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'country': 'Country'
        }