from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.contrib.auth.models import User,Group
from django.urls import reverse

class Blog(models.Model):
    title = CharField(max_length=200)
    date_added = DateTimeField(auto_now=True)
    content = TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

   

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk} )

class Comment(models.Model):
    date_added = DateTimeField(auto_now_add=True)
    content = TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
   

    def __str__(self):
        return self.content + ' | ' + str(self.blog)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk} )

    class Meta:
       ordering = ['-date_added']

    
    
    






# Create your models here.
