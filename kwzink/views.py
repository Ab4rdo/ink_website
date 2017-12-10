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
            sender_email = settings.EMAIL_HOST_USER
            receiver_email = settings.EMAIL_HOST_USER
            contact_message = "From: %s %s\nSubject: %s\nMessage:\n%s"%(
                    form_name_surname,
                    form_email,
                    form_subject,
                    form_message,
            )
            try:
                send_mail(form_subject, contact_message, sender_email, [receiver_email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('bad header found.')
    return render(request, 'kwzink/contact.html', {'form':form})

