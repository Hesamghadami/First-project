from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustumUser




class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    

class Tags(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length= 255)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    counted_comment = models.IntegerField(default=0)
    #comment
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to= 'blog', default= 'default.jpg')
    author = models.ForeignKey(CustumUser, on_delete= models.CASCADE)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tags)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title



    class Meta:
        ordering = ('-created_date',)



class Comments(models.Model):
    which_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return self.name
    


class Replay(models.Model):
    which_comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return str(self.which_comment)





