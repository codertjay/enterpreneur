from django.urls import path
from.views import *

app_name = 'codertjay'
urlpatterns =[
    path('',home_page, name='home_page'),
    path('contact/',contact_page, name='contact_page'),
    path('about/',about_page, name='about_page'),
]

