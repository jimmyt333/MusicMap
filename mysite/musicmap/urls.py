from django.urls import path, include
from musicmap import views

urlpatterns = [
    path('', views.index, name = "content"),
    path('blog/', views.blog_home, name = "blog"),
    path('about/', views.about, name = "about")


]