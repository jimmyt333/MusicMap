from django import forms
from django.forms import ModelForm
from musicmap.models import Blog, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BlogForm(forms.ModelForm):
    

    class Meta:
        model = Blog
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    

    class Meta:
        model = Comment
        fields = ['content']


class CreateUserForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

