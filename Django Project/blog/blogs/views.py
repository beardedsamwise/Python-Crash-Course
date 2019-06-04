from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """the home page for the blog"""
    posts = BlogPost.objects.all()
    context = {'posts' : posts}
    return render(request, 'blogs/index.html', context)

def newblog(request):
    """Form for users to add new blog posts."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
        
    context = {'form': form}
    return render(request, 'blogs/newblog.html', context)

def editblog(request, entry_id):
    """Edit an existing blog entry."""
    entry = BlogPost.objects.get(id=entry_id)
    post = BlogPost.objects.all()

    if request.method != 'POST':
        # Initial request, pre-fill form with the current entry.
        form = BlogForm(instance=entry)
    else:
        # POST submitted data; process data.
        form = BlogForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
        
    context = {'entry': entry, 'form': form}
    return render(request, 'blogs/editblog.html', context)
    

