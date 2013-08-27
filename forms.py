from django.db import models
from django import forms
from datetime import datetime
from django.conf import settings
from .models import Participant
from django.forms import widgets, extras
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat

class EntryForm(forms.ModelForm):

    last_name = forms.CharField(
    	label='Last Name',
    	widget = forms.TextInput(attrs={'class': 'input-block-level', 'placeholder': 'Last Name',}),
    )

    first_name = forms.CharField(
    	label='First Name',
    	widget = forms.TextInput(attrs={'class': 'input-block-level', 'placeholder': 'First Name',}),
    )

    email = forms.EmailField(
        label='Email',
        widget = forms.TextInput(attrs={'class': 'input-block-level', 'placeholder': 'Email',}),
    )

    contact = forms.IntegerField(
        label='Contact',
        widget = forms.TextInput(attrs={'class': 'input-block-level', 'placeholder': 'Contact',}),
    )

    birthday = forms.DateField(
        label='Birthday',
        widget=extras.SelectDateWidget(years=[y for y in range(1905, datetime.now().year)]),
    )

    media = forms.FileField(
        label='Select a file',
        help_text='max. 5MB',
        # widget = forms.FileInput(attrs={'class': 'input-block-level', 'accept': '.jpg, .png',})
    )

    class Meta:
        model = Participant
        exclude = ('confirmed', 'key', 'age', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Participant.objects.filter(email=email).count():
            raise forms.ValidationError(u'This email address already exist.')
        return email

    def clean_media(self):
        media = self.cleaned_data.get('media')
        try:
            if media:
                file_type = media.content_type.split('/')[0]
                print file_type

                if len(media.name.split('.')) == 1:
                    raise forms.ValidationError(u'File type is not supported.')

                if file_type in settings.UPLOAD_FILE_TYPES:
                    if media._size > settings.UPLOAD_FILE_MAX_SIZE:
                            raise forms.ValidationError(u'Please keep filesize under %s. Current filesize %s.') % (filesizeformat(settings.UPLOAD_FILE_MAX_SIZE), filesizeformat(media._size))
                else:
                    raise forms.ValidationError(u'File type is not supported.')
        except:
            pass

        return media

