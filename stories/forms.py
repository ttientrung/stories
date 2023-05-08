from django import forms
from .models import Contact
from django.core.validators import RegexValidator

class FormContact(forms.ModelForm):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name',
        'class': 'form-control fh5co_contact_text_box',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control fh5co_contact_text_box',
    }))
    subject = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'class': 'form-control fh5co_contact_text_box',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message',
        'class': 'form-control fh5co_contact_text_message',
    }))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        # exclude = ['created']