from django.db import models

# Create your models here.

class Gallery(models.Model):
    description=models.CharField(default='在这里写影片的描述',max_length=100)
    image=models.ImageField(default='default.gif',upload_to='images/')
    director=models.CharField(default='这里写影片的导演',max_length=100)
    title=models.CharField(default='影片标题',max_length=50)

    def __str__(self):
        return self.title