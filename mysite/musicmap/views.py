from django.shortcuts import render, redirect
from .models import *
from .forms import BlogForm, CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context = {}
    return render(request, 'musicmap/content.html', context) 
    #Changed html directory from maincontent to base


def blog_home(request):
    posts = Blog.objects.all()
    form = BlogForm()
    if request.method == 'POST':
        print("before form is valid")
        if form.is_valid():
            print('it is coming to the form')
            form.save()
        return redirect('/blog/')
    context = {'posts': posts, 'form':form}
    return render(request, 'musicmap/blog.html', context)



def edit_blog(request):

    pass


def delete_blog(request):

    pass





def about(request):
    context  = {}
    return render(request, 'musicmap/about.html', context)




def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')


    context = {'form': form}

    return render(request, 'musicmap/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('content')


    context = {}

    return render(request, 'musicmap/login.html', context)



@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')