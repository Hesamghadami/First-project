from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from advertisment.models import AdvertisModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import *

def blog_home(req, tag=None, username=None, cat=None):
    posts = Post.objects.filter(status=True)
    category = Category.objects.all()
    tags = Tags.objects.all()
    last_four_posts = posts[:4]
    adv = AdvertisModel.objects.all()[3]

    if tag:
         posts = Post.objects.filter(tag__name=tag)


    if username:
         posts = Post.objects.filter(author__username=username)
        
    if cat:
         posts = Post.objects.filter(category__name=cat)

    if req.GET.get('search'):
         posts = Post.objects.filter(content__contains=req.GET.get('search'))

    posts = Paginator(posts, 2)

    try:
         page_number = req.GET.get('page')
         posts = posts.get_page(page_number)


    except PageNotAnInteger:
         posts = posts.get_page(1)
     
    except EmptyPage:
         posts = posts.get_page(1)
         
    context = {
        'posts' : posts,
        'category' : category,
        'last_four_posts' : last_four_posts,
        'tags' : tags,
        'ADV' : adv,
    }
    return render(req, 'blog/blog-home.html', context=context)


def blog_single(req, pid):
     if req.method == 'GET':
          post_list_id = []
          posts = Post.objects.filter(status=True)
          for post in posts:
               post_list_id.append(post.id)


          post_list_id.reverse()

          if post_list_id.index(pid) == 0:
               previous_post = None
               next_post = posts.get(id=post_list_id[1])
          elif post_list_id.index(pid) == post_list_id.index(post_list_id[-1]):
               previous_post = posts.get(id=post_list_id[-2])
               next_post = None

          else:
               next_post = posts.get(id=post_list_id[post_list_id.index(pid)+1])
               previous_post =  posts.get(id=post_list_id[post_list_id.index(pid)-1])



          try :
               comments = Comments.objects.filter(which_post=pid, status=True)
               replay = Replay.objects.all()
               post = Post.objects.get(id=pid, status=True)
               post.counted_views += 1
               post.save()
               context = {
                    'post': post,
                    'next' : next_post,
                    'prev' : previous_post,
                    'comments': comments,
                    'replay' : replay,
                    }
               return render(req, 'blog/blog-single.html', context=context)
          except:
               return render(req, 'blog/404.html')
     elif req.method == 'POST':
          form = CommentForm(req.POST)
          print (req.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
          

def replay(req, cid):
     comment = Comments.objects.get(id=cid)
     if req.method == 'GET':
          context = {
               'comment' : comment,
          }
          return render(req, 'blog/edit.html', context=context)   
     
     elif req.method == 'POST':
          form = ReplayForm(req.POST)
          if form.is_valid():
               form.save()
               return redirect('/blog/')
          

def delete(req, cid):

     comment = Comments.objects.get(id=cid)
     comment.delete()
     return redirect('/')   
     

def edit(req, cid):
     comment = Comments.objects.get(id=cid)
     if req.method == 'GET':
          
          form = CommentForm(instance=comment)
          context = {
               'form' : form,
          }
          return render(req,'blog/commentedit.html',context=context)
     elif req.method == "POST" :
          form = CommentForm(req.POST, instance=comment)
          if form.is_valid():
               form.save()
               return redirect('/blog/')
          

def add(req):
     if req.method == 'GET':
          context = {
               'form' : PostForm()
          }
          return render(req,'blog/add.html',context=context)
     elif req.method == 'POST':
          form = PostForm(req.POST, req.FILES)
          if form.is_valid():
               form.save()
               return redirect('/blog/')







