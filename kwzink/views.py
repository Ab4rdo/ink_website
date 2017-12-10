from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

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
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['fryderyk97@gmail.com'])
            except BadHeaderError:
                return HttpResponse('bad header found.')
    return render(request, 'kwzink/contact.html', {'form':form})

