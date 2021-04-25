from django.urls import path, include
from musicmap import views
from .views import (PostListView, PostDetailView,
                    PostCreateView, PostUpdateView, PostDeleteView, AddCommentView, EditCommentView, DeleteCommentView )

urlpatterns = [
    path('', views.index, name="content"),
    # path('blog/', views.blog_home, name = "blog"),

    path('blog/', PostListView.as_view(), name="blog"),
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    
    path('blog/post/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('blog/post/<int:pk>/edit_comment/', EditCommentView.as_view(), name="edit_comment"),
    path('blog/post/<int:pk>/delete_comment/', DeleteCommentView.as_view(), name="delete_comment"),


    path('blog/post/new/', PostCreateView.as_view(), name="post-create"),
    path('blog/post/<int:pk>/edit/', PostUpdateView.as_view(), name="post-edit"),
    path('blog/post/<int:pk>/delete/',
         PostDeleteView.as_view(), name="post-delete"),


    path('about/', views.about, name="about"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout")

    # <app>/<model>_ blog_delail.html
    #
]
