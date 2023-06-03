from django.contrib import admin
from .models import *



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['status', 'created_date']
    list_filter = ['status']
    search_fields = ['title']
    empty_value_display = 'empty value'


admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comments)

admin.site.register(Replay)


# Register your models here.
