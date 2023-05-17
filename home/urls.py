from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
    path('', home, name= 'home'),
    path('contact', contact, name = 'contact'),
    path('about', about , name = 'about'),
]