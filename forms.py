from django.db import models
from django import forms
from .models import Participant
from django.forms import widgets

class EntryForm(forms.ModelForm):

    email = forms.EmailField(
    	label='Email',
    	widget = forms.TextInput(attrs={'class': 'input-block-level', 'placeholder': 'Email',})
    )

    last_name = forms.CharField(
    	label='Last Name',
    	widget = forms.TextInput(attrs={'class': 'input-block-level', 'placeholder': 'Last Name',})
    )

    first_name = forms.CharField(
    	label='First Name',
    	widget = forms.TextInput(attrs={'class': 'input-block-level', 'placeholder': 'First Name',})
    )

    class Meta:
        model = Participant
        exclude = ('username', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined', 'initial-date_joined', 'confirmation_code', 'time', 'confirmed', 'key',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Participant.objects.filter(email=email).count():
            raise forms.ValidationError(u'The email address already exist.')
        return email

