from django.urls import include, path

#from ink_website import settings

from . import views

app_name = 'kwzink'

urlpatterns = [
    path('', views.index, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('inks/', views.inks, name="inks"),
    ]
