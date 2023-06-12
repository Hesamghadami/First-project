from django import template
from blog.models import Post
from home.models import LuxurayPackage


register = template.Library()

@register.simple_tag(name='Last_six')
def Last_six(number:int):
    last_six = Post.objects.filter(status=True)[:number]
    return last_six


@register.filter(name='upper')
def Upper(text:str):
    return text.upper()


@register.filter(name='trruncate')
def Trruncate(text:str,number:int):
    return ' '.join(text.split()[:number])


@register.inclusion_tag('issue.html')
def Issue ():
    pass

@register.inclusion_tag('lux.html')
def lux ():
    luxuray = LuxurayPackage.objects.all()
    return {'luxury':luxuray}
    


