from django.db import models

class BlogPost(models.Model):
    """An entry in the blog"""
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64,unique=True)
    text = models.TextField(max_length=400)
    
    def __str__(self):
        return self.title