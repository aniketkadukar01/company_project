from django.urls import path
from .views import index, contact_form

urlpatterns = [
    path('index/', index, name='index'),
    path('contact/', contact_form, name='contact_form'),
]
