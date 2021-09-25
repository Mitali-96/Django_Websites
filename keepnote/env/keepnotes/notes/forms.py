from django import forms
from .models import Notes
from django.contrib.auth.models import User
class NoteCreationForm(forms.ModelForm):

    class Meta:
        model=Notes
        fields=['title','description']

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']

class AccountSettingsForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name']
