from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """An entry in the blog"""
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64,unique=True)
    text = models.TextField(max_length=400)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title