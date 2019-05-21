from django import forms
from django.core import validators

class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_mail = forms.EmailField()
    text=forms.CharField()

    def clean(self):
        all_clean_data=super().clean()
        email = all_clean_data.get('email')
        #print("hi")
        vmail = all_clean_data.get('verify_email')
        #print("hello")

        if email != vmail:
            raise forms.ValidationError("Make sure email matches ")
