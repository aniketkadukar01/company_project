from django.urls import path
from .views import (
    index, 
    contact_form, 
    blog_detail, 
    blogs,
)

urlpatterns = [
    path('index/', index, name='index'),
    path('contact/', contact_form, name='contact_form'),
    path('blog_detail/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('blogs/', blogs, name='blogs'),
]
