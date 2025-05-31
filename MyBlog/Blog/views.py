from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Category, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts, 'categories':categories, 'tags':tags }) 

def post_details(request, id):
    post = get_object_or_404(Post, id = id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/post_details.html', {'post': post, 'categories':categories, 'tags':tags})

def signup_view(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
