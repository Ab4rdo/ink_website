from django import forms

class ContactForm(forms.Form):
    
    name_surname = forms.CharFiled(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)

