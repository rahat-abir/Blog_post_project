from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField( max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField( max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True, blank = True)
    tag = models.ManyToManyField(Tag, blank= True)

    def __str__(self):
        return self.title