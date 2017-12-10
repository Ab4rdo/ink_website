from django.urls import path

from . import views

app_name = 'kwzink'

urlpatterns = [
    path('', views.index, name='home'), # home dir
    path('contact/', views.contact, name='contact'), 
    path('about/', views.about, name='about'),
#   path('form', views.form),
#   path('inks', views.inks),
#   path('inks/ig', views.ig),
#   path('inks/standard', views.standard),
]
