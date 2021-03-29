from django.urls import path, include
from musicmap import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.index, name = "content"),
    path('blog/', PostListView.as_view(), name = "blog"),
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name = "post-detail"),
    path('blog/post/new/', PostCreateView.as_view(), name = "post-create"),
    path('blog/post/<int:pk>/edit/', PostUpdateView.as_view(), name = "post-edit"),
    path('blog/post/<int:pk>/delete/', PostDeleteView.as_view(), name = "post-delete"),


    path('about/', views.about, name = "about"),
    path('register/',views.registerPage, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout")



]