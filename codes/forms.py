from django import forms
from .models import Codes
class CodeForm(forms.ModelForm):
    number=forms.CharField(label='code', help_text='Enter your sms  verification code')
    class Meta:
        model=Codes
        fields=('number' ,)
         