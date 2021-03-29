from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import *
from .forms import BlogForm, CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# Create your views here.

def index(request):
    context = {}
    return render(request, 'musicmap/content.html', context) 
    #Changed html directory from maincontent to base

def blogPosts(request):
    context = {'posts': Blog.objects.all()}

    return render(request, 'musicmap/blog.html', context)



class PostListView(ListView):
    model = Blog
    template_name = 'musicmap/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Blog


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False

class PostDeleteView(UserPassesTestMixin, UserPassesTestMixin, DeleteView ):
    model = Blog
    success_url = '/blog'

    def test_func(self):
            post = self.get_object()
            if self.request.user == post.auther:
                return True
            return False



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