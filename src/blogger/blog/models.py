from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):

    title           = models.CharField(max_length=100)
    content         = models.TextField()
    created_date    = models.DateTimeField(default=timezone.now)
    updated_date    = models.DateTimeField(auto_now=True)
    image           = models.ImageField(upload_to='blog/static/images/')
    auther          = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

    #make order articles from last to old
    class Meta:
        ordering = ('-created_date',)
        

