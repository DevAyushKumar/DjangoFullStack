from django.shortcuts import render
from .models import post

def home(response):
    context = {
        'post' : post.objects.all()
    }
    return render(response, 'blog/home.html',context,)

def about(response):
    return render(response, 'blog/about.html', )