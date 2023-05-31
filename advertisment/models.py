from django.db import models

class AdvertisModel(models.Model):
    title = models.CharField(max_length=255, default='empty')
    image = models.ImageField(upload_to='images',default='default2.jpg')
    link = models.CharField(max_length=255, default='#')

    def __str__(self) -> str:
        return self.title
    



# Create your models here.
