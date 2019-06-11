from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """the home page for the blog"""
    posts = BlogPost.objects.all()
    context = {'posts' : posts}
    return render(request, 'blogs/index.html', context)

@login_required
def newblog(request):
    """Form for users to add new blog posts."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:index'))
        
    context = {'form': form}
    return render(request, 'blogs/newblog.html', context)

@login_required
def editblog(request, entry_id):
    """Edit an existing blog entry."""
    entry = BlogPost.objects.get(id=entry_id)
    post = BlogPost.objects.all()
    if entry.owner != request.user:
        raise Http404
    else:
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
    

