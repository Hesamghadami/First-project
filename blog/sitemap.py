from django.urls import reverse
from django.contrib import sitemaps
from .models import Post




class DynamicSiteMaps(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Post.objects.filter(status=True).order_by('created_date')
    
    def location(self, obj):
        return 'blog/post_details/%s'%obj.id
