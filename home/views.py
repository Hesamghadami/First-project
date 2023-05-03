from django.shortcuts import render
from .models import student

def home(req):
    return render(req, 'home/index.html')

def about(req):
    return render(req, 'home/about.html')

def contact(req):
    return render(req, 'home/contact.html')

def test(req):
    students = student.objects.all()[2]
    context = {
        'students' : students
    }
    return render(req, 'home/test.html', context = context)

def blog_home(req):
    return render(req, 'home/blog-home.html')

def blog_single(req):
    return render(req, 'home/blog-single.html')
