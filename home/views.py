from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(req):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render())