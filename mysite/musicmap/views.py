from django.shortcuts import render, redirect
from .models import *
from .forms import BlogForm

# Create your views here.

def index(request):
    context = {}
    return render(request, 'musicmap/content.html', context) 
    #Changed html directory from maincontent to base


def blog_home(request):
    posts = Blog.objects.all()
    form = BlogForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog/')
    context = {'posts': posts}
    return render(request, 'musicmap/blog.html', context)



def edit_blog(request):

    pass


def delete_blog(request):

    pass




def edit_blog(request):
    pass


def about(request):
    context  = {}
    return render(request, 'musicmap/about.html', context)


def register(request):
    pass

def login(request):
    pass