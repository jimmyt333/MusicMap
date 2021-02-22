from django.urls import path, include
from musicmap import views

urlpatterns = [
    path('', views.index, name = "content")
]