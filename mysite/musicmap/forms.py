from django import forms
from django.forms import ModelForm
from musicmap.models import Blog






class BlogForm(forms.ModelForm):
    

    class Meta:
        model = Blog
        fields = ['title', 'content']