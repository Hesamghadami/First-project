from django.db import models



#django-data-type
#geeksforgeeks

class CheapPackage(models.Model):
    city = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.city

class LuxurayPackage(models.Model):
    city = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.city

class CampingPackage(models.Model):
    city = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.city








    

class Post(models.Model):

    name = models.CharField(max_length= 50)
    family = models.CharField(max_length= 50)
    code = models.CharField(max_length= 12)
    def __str__(self) -> str:
        return self.city

# Create your models here.
