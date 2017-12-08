from django.conf.urls import url

from . import views

app_name = 'kwzink'

urlpatterns = [
    url('', views.index, name='index'), # home dir
#   path('contact', views.contact),
#   path('about', views.about),
#   path('form', views.form),
#   path('inks', views.inks),
#   path('inks/ig', views.ig),
#   path('inks/standard', views.standard),
]
