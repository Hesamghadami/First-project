from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
    path('', home, name= 'home'),
    path('contact', contact, name = 'contact'),
    path('about', about , name = 'about'),
    path('test', test , name = 'test'),
    path('blog-home', blog_home , name = 'blog-home'),
    path('blog-single', blog_single , name = 'blog-single'),
]