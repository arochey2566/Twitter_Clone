from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, PictureForm
from django.shortcuts import render
# from django.urls import reverse_lazy, reverse
# from cloudinary.forms import cl_init_js_callbacks


def index(request):
    # if the method is post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #if the method is valid
        if form.is_valid():
            #Yes, Save
            form.save()
            #redirect to home
            return HttpResponseRedirect('/')
        else:
            #if not, show error
            return HttpResponseRedirect(form.errors.as_json())
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form = PostForm()
    # Show
    return render(request, 'posts.html', 
                        {'posts': posts})


#delete
def delete(request, post_id):
    # Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')


#edit  

def edit(request, post_id):
    posts = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form= PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("not valid")
    form = PostForm
    return render(request, 'edit.html', {'posts': posts})


#like
def like(request, post_id):
    newlikecount = Post.objects.get(id=post_id)
    newlikecount.like += 1
    newlikecount.save()
    return HttpResponseRedirect('/')
