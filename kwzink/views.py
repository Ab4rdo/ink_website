from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from ink_website import settings
from .forms import ContactForm

def index(request):
    return render(request, 'kwzink/index.html')

def contact(request):
    return email(request)

def about(request):
    return render(request, 'kwzink/about.html')

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form_name_surname = form.cleaned_data['name_surname']
            form_email = form.cleaned_data['email']
            form_subject = form.cleaned_data['subject']
            form_message = form.cleaned_data['message']
            email = settings.EMAIL_HOST_USER
            email_subject = form_name_surname + ': ' + form_subject
            contact_message = "From: %s %s\n\nMessage:\n%s"%(
                    form_name_surname,
                    form_email,
                    form_message,
            )
            try:
                send_mail(email_subject, contact_message, email, [email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('bad header found.')
    return render(request, 'kwzink/contact.html', {'form':form})

