from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Create your views here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 30)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add= True)
    date_updated = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title