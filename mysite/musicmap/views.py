from mysite.settings import SPOTIFY_CREDENTIALS
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import *
from .forms import BlogForm, CreateUserForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .spotifyClient import SpotifyClient
import json



# Create your views here.
def index(request):
    musicMap = None
    relationGraph = None

    if request.method == "POST":
        searchString = request.POST.get('searchString')
        # open credentials json and read api keys
        with open(SPOTIFY_CREDENTIALS + 'credentials.json') as tokens:
            keys = json.load(tokens)

        # connect to Spotify API
        client_id = keys["client_Id"]
        client_secret = keys["client_secret"]

        # create spotifyClient object
        spottyClient = SpotifyClient(client_id, client_secret)

        musicMap = spottyClient.createMusicMap(searchString)

        # check if searchString is valid
        if(musicMap):
            relationGraph = musicMap.getGraph()
        else:
            errorMsg = "Please enter a valid artist name."
            relationGraph = None
            context = {'relationGraph': relationGraph,
                    'musicMap': musicMap, 'errorMsg': errorMsg, 'errorFlag': 1}
            return render(request, 'musicmap/content.html', context)

    elif request.method == "GET" and 'artist_musicMap' in request.GET:

        searchString = str(request.GET.get('artist_musicMap'))

        # open credentials json and read api keys
        with open(SPOTIFY_CREDENTIALS + 'credentials.json') as tokens:
            keys = json.load(tokens)

        # connect to Spotify API
        client_id = keys["client_Id"]
        client_secret = keys["client_secret"]

        # create spotifyClient object
        spottyClient = SpotifyClient(client_id, client_secret)

        musicMap = spottyClient.createMusicMap(searchString)
        relationGraph = musicMap.getGraph()

    context = {'relationGraph': relationGraph,
            'musicMap': musicMap, 'errorFlag': 0}
    return render(request, 'musicmap/content.html', context)
 


class PostListView(ListView):
    model = Blog
    template_name = 'musicmap/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_added']

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
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView ):
    model = Blog
    success_url = '/blog'

    def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False





class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'musicmap/comment_form.html'
    form_class = CommentForm
    success_url = '/blog'
    ordered_tasks = Comment.objects.order_by('-date_added')

    
    def form_valid(self, form):

        form.instance.blog_id = self.kwargs['pk'] 
        form.instance.author = self.request.user        
        return super().form_valid(form)


class EditCommentView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    success_url = '/blog'


    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog_id = self.kwargs['pk'] 
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView ):
    model = Comment
    success_url = '/blog'

    def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
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