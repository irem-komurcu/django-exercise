from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=120,verbose_name='başlık')
    content=models.TextField(verbose_name='içerik')
    publishing_date=models.DateTimeField(verbose_name='yayınlanma tarihi',auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})
        #  return "/post/{}".format(self.id)