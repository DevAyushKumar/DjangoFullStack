from django.shortcuts import render
from .models import posts

def home(response):
    context = {
        'posts' : posts.objects.all()
    }
    return render(response, 'blog/home.html',context,)

def about(response):
    return render(response, 'blog/about.html', )