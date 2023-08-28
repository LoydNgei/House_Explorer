# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        """Meta is used to specify the model and fields that will be used in the form"""
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
