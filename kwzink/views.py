from django.shortcuts import render

def index(request):
    return render(request, 'kwzink/index.html')

def contact(request):
    return render(request, 'kwzink/contact.html')

def about(request):
    return render(request, 'kwzink/about.html')
