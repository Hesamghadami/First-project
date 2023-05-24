from django.shortcuts import render
from .models import *

def blog_home(req, tag = None,  username = None, cat = None):
    posts = Post.objects.filter(status = True)
    category = Category.objects.all()

    last_four_posts = posts[:4]

    if tag:
        posts = Post.objects.filter(tag__name = tag)

    if username:
        posts = Post.objects.filter(author__username = username)
    if cat:
        posts = Post.objects.filter(category__name = cat)


    if req.GET.get('search'):
        posts = Post.objects.filter(content__contains = req.GET.get('search'))






    context = {
        'posts': posts,
        'category':category,
        'last_four_posts':last_four_posts,
    }
    return render(req, 'blog/blog-home.html', context = context)

def blog_single(req):
    return render(req, 'blog/blog-single.html')








