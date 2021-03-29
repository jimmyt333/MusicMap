from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.contrib.auth.models import User
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
    
    
    






# Create your models here.
