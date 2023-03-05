from django.http import HttpResponse


def home(req):
    return HttpResponse("Welcom to my website")

def contact(req):
    return HttpResponse("Contact us")

def about_us(req):
    return HttpResponse("About us")


def hi(req):
    return HttpResponse("Hi")
