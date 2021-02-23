from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'musicmap/base.html', context) 
    #Changed html directory from maincontent to base
