from django import forms
from captcha.fields import ReCaptchaField

class ContactForm(forms.Form):

    name_surname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(attrs={
         'theme' : 'light',
         })

