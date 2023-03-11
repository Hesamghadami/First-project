from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse


def home(req):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render())

def contact(req):
    return HttpResponse("Contact us")

def about_us(req):
    return HttpResponse("About us")


def hi(req):
    return HttpResponse("Hi")
