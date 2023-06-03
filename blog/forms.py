from django import forms
from .models import *



class CommentForm(forms.ModelForm):


    class Meta:
        model = Comments
        fields = ['which_post', 'name', 'email', 'subject', 'message']


class ReplayForm(forms.ModelForm):


    class Meta:
        model = Replay
        fields = ['which_comment', 'message']


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'author', 'category', 'tag', 'published_date']