from django.db import models

class student(models.Model):

    name = models.CharField(max_length= 50)
    family = models.CharField(max_length= 50)
    code = models.CharField(max_length= 12)
    def __str__(self) -> str:
        return self.name

# Create your models here.
