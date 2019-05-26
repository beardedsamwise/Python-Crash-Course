from django.db import models

class BlogPost(models.Model):
    """A blog post for the Python blog"""
    title = models.CharField(max_length=100)
    text = models.TextField
    date_added = models.DateTimeField(auto_now_add=True)
          
