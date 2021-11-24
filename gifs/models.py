from django.db import models

# Create your models here.
class Gif_Model(models.Model):
    title = models.CharField(max_length = 100)
    url = models.URLField(max_length = 100)
    uploader_name = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField(default = 0)

class Category(models.Model):
    name = models.CharField(max_length = 100)
    gifs = models.ManyToManyField(Gif_Model, related_name='gifs')

