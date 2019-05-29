from django.shortcuts import render

from .models import BlogPost

def index(request):
    """the home page for the blog"""
    posts = BlogPost.objects.all()
    context = {'posts' : posts}
    return render(request, 'blogs/index.html', context)
