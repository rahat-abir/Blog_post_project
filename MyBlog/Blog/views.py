from django.shortcuts import render
from .models import Post, Category, Tag
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blog/base.html', {'posts': posts, 'categories':categories, 'tags':tags }) 
