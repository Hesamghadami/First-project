from django.shortcuts import render
from .models import *

def blog_home(req):
    posts = Post.objects.filter(status = True)
    context = {
        'posts': posts
    }
    return render(req, 'blog/blog-home.html', context = context)
def blog_single(req):
    return render(req, 'blog/blog-single.html')







