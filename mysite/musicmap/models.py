from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.contrib.auth.models import User

class Blog(models.Model):
    title = CharField(max_length=200)
    date_added = DateTimeField(auto_now=True)
    content = TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta():
        ordering = ['-date_added']

    def __str__(self):
        return self.title






# Create your models here.
